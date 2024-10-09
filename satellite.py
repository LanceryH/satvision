import numpy as np
import pytz
from datetime import datetime, timezone
from dataclasses import dataclass, field

@dataclass
class VEC_3:
    XYZ : np.ndarray
    
    @property
    def X(self):
        return self.XYZ[0,:]
    
    @property
    def Y(self):
        return self.XYZ[1,:]
    
    @property
    def Z(self):
        return self.XYZ[2,:]

@dataclass
class VEC_2:
    LON_LAT : np.ndarray
    
    @property
    def LON(self):
        return self.LON_LAT[0,:]
    
    @property
    def LAT(self):
        return self.LON_LAT[1,:]
 
@dataclass
class Position:
    orbital : VEC_3 = field(init=False)
    inertial : VEC_3 = field(init=False)
    geografic : VEC_2 = field(init=False)
    geoorbit : VEC_3 = field(init=False)
    plot : VEC_2 = field(init=False)
    
@dataclass
class Speed:
    orbital : VEC_3 = field(init=False)
    inertial : VEC_3 = field(init=False)

@dataclass
class Satellite:
    NAME: str
    NORA_ID: int
    EPOCH: str
    MEAN_MOTION: float
    ECCENTRICITY: float
    INCLINATION: float
    RA_OF_ASC_NODE: float
    ARG_OF_PERICENTER: float
    MEAN_ANOMALY: float
    MUE: float = 398600.44
    EARTH_MASS: float = 5.972e24
    G: float = 6.67384e-11
    NB_ORBITS: int = 1
    NB_POINTS: int = 50
    TIME_SIMU_START: int = '09.10.2024 22:48:42'
    TIME_SIMU_END: int = '09.10.2024 23:48:42'
    position = Position
    speed = Speed
    
    d1: datetime = field(init=False)
    dt: float = field(init=False)
    PERIOD: float = field(init=False)
    time: np.ndarray = field(init=False)
    MEAN_ANOMALY_future: np.ndarray = field(init=False)

    def __post_init__(self):
        self.PERIOD = (1 / self.MEAN_MOTION) * 86400  # seconds in a day
        self.SIMU_DURATION = (datetime.strptime(self.TIME_SIMU_END, '%d.%m.%Y %H:%M:%S.%f') - datetime.strptime(self.TIME_SIMU_START, '%d.%m.%Y %H:%M:%S.%f')).total_seconds()
        self.parse_epoch()
        self.convert_degrees_to_radians()
        self.calculate_orbital_parameters()
        self.initial_state_parameters()

    def parse_epoch(self):
        self.d1 = datetime.strptime(self.EPOCH, '%Y-%m-%dT%H:%M:%S.%f')
        self.d2 = datetime.strptime(self.TIME_SIMU_START, '%d.%m.%Y %H:%M:%S.%f')
        self.dt = (self.d2 - self.d1).total_seconds()

    def convert_degrees_to_radians(self):
        self.ECCENTRICITY = np.deg2rad(self.ECCENTRICITY)
        self.INCLINATION = np.deg2rad(self.INCLINATION)
        self.RA_OF_ASC_NODE = np.deg2rad(self.RA_OF_ASC_NODE)
        self.ARG_OF_PERICENTER = np.deg2rad(self.ARG_OF_PERICENTER)
        self.MEAN_ANOMALY = np.deg2rad(self.MEAN_ANOMALY)

    def calculate_orbital_parameters(self):
        if self.SIMU_DURATION != 0:
            self.time = np.linspace(0, self.SIMU_DURATION, self.NB_POINTS)
        else:
            self.NB_POINTS = 1
            self.time = np.linspace(0, 1, self.NB_POINTS)
        self.MEAN_MOTION_SI = 2 * np.pi / self.PERIOD
        self.SEMI_MAJOR_AXIS = ((self.MUE / (self.MEAN_MOTION_SI ** 2)) ** (1 / 3)) * 1000
        self.MEAN_MOTION = np.sqrt(self.EARTH_MASS * self.G / self.SEMI_MAJOR_AXIS ** 3)
        self.MEAN_ANOMALY += self.MEAN_MOTION * self.dt

    def calcul_orbital_mecanic(self, ANOMALY):
        r = self.SEMI_MAJOR_AXIS * (1 - self.ECCENTRICITY * np.cos(ANOMALY))
        cos_E = np.cos(ANOMALY)
        sin_E = np.sin(ANOMALY)
        x = self.SEMI_MAJOR_AXIS * (cos_E - self.ECCENTRICITY)
        y = self.SEMI_MAJOR_AXIS * np.sqrt(1 - self.ECCENTRICITY**2) * sin_E
        xdot = -sin_E * self.MEAN_MOTION * self.SEMI_MAJOR_AXIS**2 / r
        ydot = np.sqrt(1 - self.ECCENTRICITY**2) * cos_E * self.MEAN_MOTION * self.SEMI_MAJOR_AXIS**2 / r
        return np.vstack((x, y, np.zeros_like(ANOMALY))), np.vstack((xdot, ydot, np.zeros_like(ANOMALY)))
    
    def calcul_inertial_mecanic(self, ANOMALY, i):
        R_total = self.R_RA_OF_ASC_NODE @ self.R_INCLINATION @ self.R_ARG_OF_PERICENTER
        xyz = self.ROT_EARTH(self.time[i]) @ R_total @ self.calcul_orbital_mecanic(ANOMALY)[0]
        xyzdot = self.ROT_EARTH(self.time[i]) @ R_total @ self.calcul_orbital_mecanic(ANOMALY)[1]
        return xyz.reshape(3,1), xyzdot.reshape(3,1)
    
    def calcul_geografic_mecanic(self, ANOMALY, i):
        xyz = self.calcul_inertial_mecanic(ANOMALY, i)[0]
        p=np.linalg.norm(xyz,axis=0)
        a = 6378137
        b = 6356752.314235
        f = (a - b) / a
        lon = np.rad2deg(np.arctan2(xyz[1],xyz[0]))-self.GMST
        lat = np.rad2deg(np.arcsin(xyz[2]/p))* (1 - f * f)
        if lon > 180:
            lon -= 360
        elif lon < -180:
            lon += 360
        return np.vstack((lon,lat)),p

    def calcul_geoorbit_mecanic(self, ANOMALY, i):
        lon_lat, alt = self.calcul_geografic_mecanic(ANOMALY, i)
        x = np.cos(np.deg2rad(lon_lat[1]))*np.sin(np.deg2rad(lon_lat[0]))*alt/1000
        y = np.sin(np.deg2rad(lon_lat[1]))*alt/1000
        z = np.cos(np.deg2rad(lon_lat[1]))*np.cos(np.deg2rad(lon_lat[0]))*alt/1000
        return np.vstack((x,y,z))
    
    def initial_state_parameters(self):   
        #self.position.orbital = VEC_3(self.calcul_orbital_mecanic(self.MEAN_ANOMALY)[0])
        #self.speed.orbital = VEC_3(self.calcul_orbital_mecanic(self.MEAN_ANOMALY)[1])
        #self.position.inertial = VEC_3(self.calcul_inertial_mecanic(self.MEAN_ANOMALY, 0)[0])
        #self.speed.inertial = VEC_3(self.calcul_inertial_mecanic(self.MEAN_ANOMALY, 0)[1])
        #self.position.geografic = VEC_2(self.calcul_geografic_mecanic(self.MEAN_ANOMALY, 0)[0])
        self.position.geoorbit = VEC_3(self.calcul_geoorbit_mecanic(self.MEAN_ANOMALY, 0))
        #self.position.plot = self.position.geografic
        pass
        
    
    @property
    def R_INCLINATION(self) -> np.ndarray:
        return np.array([[1, 0, 0],
                         [0, np.cos(-self.INCLINATION), np.sin(-self.INCLINATION)],
                         [0, -np.sin(-self.INCLINATION), np.cos(-self.INCLINATION)]])

    @property
    def R_RA_OF_ASC_NODE(self) -> np.ndarray:
        return np.array([[np.cos(-self.RA_OF_ASC_NODE), np.sin(-self.RA_OF_ASC_NODE), 0],
                         [-np.sin(-self.RA_OF_ASC_NODE), np.cos(-self.RA_OF_ASC_NODE), 0],
                         [0, 0, 1]])

    @property
    def R_ARG_OF_PERICENTER(self) -> np.ndarray:
        return np.array([[np.cos(-self.ARG_OF_PERICENTER), np.sin(-self.ARG_OF_PERICENTER), 0],
                         [-np.sin(-self.ARG_OF_PERICENTER), np.cos(-self.ARG_OF_PERICENTER), 0],
                         [0, 0, 1]])
    @property
    def GMST(self) -> float:
        a = (14 - self.d1.month) // 12
        y = self.d1.year + 4800 - a
        m = self.d1.month + 12 * a - 3
        JD = (self.d1.day + ((153 * m + 2) // 5) + 365 * y + (y // 4) - (y // 100) + (y // 400) - 32045 +
            (self.d1.hour - 12) / 24.0 + self.d1.minute / 1440.0 + self.d1.second / 86400.0)
        T = (JD - 2451545.0) / 36525.0
        GMST = (280.46061837 +
                360.98564736629 * (JD - 2451545.0) +
                T ** 2 * (0.000387933 - T / 38710000))
        GMST %= 360
        return GMST

    def ROT_EARTH(self, t) -> np.ndarray:
        fi_earth = (self.dt + t) * 2 * np.pi * (1 + 1 / 365.25) / 86400
        return np.array([[np.cos(fi_earth), np.sin(fi_earth), 0],
                         [-np.sin(fi_earth), np.cos(fi_earth), 0],
                         [0, 0, 1]])

    def future_it(self):
        self.MEAN_ANOMALY_future = self.MEAN_ANOMALY + self.MEAN_MOTION * self.time
        epsilon = 1e-10  # Plus petit seuil pour les faibles excentricités

        for i in range(self.NB_POINTS):
            M = self.MEAN_ANOMALY_future[i]
            e = self.ECCENTRICITY
            if e < 0.8:  # Pour faible excentricité, approximation initiale proche de M
                E = M
            else:  # Pour forte excentricité, une autre approximation initiale est préférable
                E = np.pi
            for _ in range(100):  # Limitation à 100 itérations maximum pour éviter des boucles infinies
                f = E - e * np.sin(E) - M
                f_prime = 1 - e * np.cos(E)
                delta = f / f_prime
                E -= delta
                
                if np.abs(delta) < epsilon:
                    break
                
            #self.position.orbital.XYZ = np.hstack((self.position.orbital.XYZ, self.calcul_orbital_mecanic(E)[0]))
            #self.speed.orbital.XYZ = np.hstack((self.speed.orbital.XYZ, self.calcul_orbital_mecanic(E)[1]))
            #self.position.inertial.XYZ = np.hstack((self.position.inertial.XYZ, self.calcul_inertial_mecanic(E, i)[0]))            
            #self.speed.inertial.XYZ = np.hstack((self.speed.inertial.XYZ, self.calcul_inertial_mecanic(E, i)[1]))
            #self.position.geografic.LON_LAT = np.hstack((self.position.geografic.LON_LAT, self.calcul_geografic_mecanic(E, i)[0]))
            self.position.geoorbit.XYZ = np.hstack((self.position.geoorbit.XYZ, self.calcul_geoorbit_mecanic(E, i)))
            
        #lon_plot = self.position.geografic.LON.tolist()
        #lat_plot = self.position.geografic.LAT.tolist()
        #for ind_i in range(0,len(lon_plot)-1):
        #    if np.abs(lon_plot[ind_i]+lon_plot[ind_i+1])<np.abs(lon_plot[ind_i]) and np.abs(lon_plot[ind_i])+np.abs(lon_plot[ind_i+1])>270:
        #        lon_plot[ind_i]=np.nan
        #        lat_plot[ind_i]=np.nan
        #self.position.plot.LON_LAT = np.vstack((lon_plot,lat_plot))