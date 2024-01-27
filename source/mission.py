import numpy as np
from parameters import *
 
class Mission_class:
    def __init__(self,
                 CLIENT="undefined",
                 ALTITUDE="undefined",
                 ROCKET="undefined"):
        self.MISSION_CHAR={"CNES": {"perigee_alt":340.0,
                                    "apogee_alt":340.0,
                                    "inclination":90.0,
                                    "latitude":60.8},
                           "Roscosmos":{"perigee_alt":410.0,
                                        "apogee_alt":410.0,
                                        "inclination":51.6,
                                        "latitude":46.0},
                           "Eutelsat":{"perigee_alt":300.0,
                                       "apogee_alt":35786.0,
                                       "inclination":5.2,
                                       "latitude":5.2},
                           "NASA":{"perigee_alt":1681.0,
                                   "apogee_alt":1681.0,
                                   "inclination":103.0,
                                   "latitude":28.5}}
        self.ROCKET = ROCKET
        self.ALTITUDE = ALTITUDE
        self.CLIENT = CLIENT
        self.PERIGEE = self.MISSION_CHAR[CLIENT]["perigee_alt"]+R_e
        self.APOGEE = self.MISSION_CHAR[CLIENT]["apogee_alt"]+R_e
        self.INCLINATION = self.MISSION_CHAR[CLIENT]["inclination"]
        self.LATITUDE = self.MISSION_CHAR[CLIENT]["latitude"]
        self.AZIMUTH = np.rad2deg(np.arcsin(np.cos(np.deg2rad(self.INCLINATION))/np.cos(np.deg2rad(self.LATITUDE))))
        self.MASS_INITIAL_1 = 0
        self.MASS_FINAL_1 = 0
        self.MASS_INITIAL_2 = 0
        self.MASS_FINAL_2 = 0
        self.MASS_INITIAL_3 = 0
        self.MASS_FINAL_3 = 0
        self.DV1 = 0
        self.DV2 = 0
        self.DV3 = 0
        self.DV = 0
        self.DV_REQUIRED = 0
        self.LOSSES = 0
        self.V_INITIAL = 0
        self.V_FINAL = 0
        self.VF = 0
        self.SEMI_MAJOR_AXIS = 0
        self.ECCENTRICITY = 0
        self.me1 = 0
        self.ms1 = 0
        self.me2 = 0
        self.ms2 = 0
        self.me3 = 0
        self.ms3 = 0
        self.m_total = 0
        self.message = ""

    def build(self, error_min=1e-6, b_last=3, pas=1):
        for index in self.ROCKET.STAGES:
            self.MASS_INITIAL_1 += index.TOTAL_MASS
        self.MASS_INITIAL_1 += self.ROCKET.PAYLOAD_MASS + self.ROCKET.FAIRING_MASS
        self.MASS_FINAL_1 = self.MASS_INITIAL_1 - self.ROCKET.STAGES[0].PROPELLANT_MASS
        self.DV1 = self.ROCKET.STAGES[0].ISP*g0*np.log(self.MASS_INITIAL_1/self.MASS_FINAL_1)

        if len(self.ROCKET.STAGES)>1 and len(self.ROCKET.STAGES)<3:
            self.MASS_INITIAL_2 = self.MASS_INITIAL_1 - self.ROCKET.STAGES[0].TOTAL_MASS - self.ROCKET.FAIRING_MASS
            self.MASS_FINAL_2 = self.MASS_INITIAL_2 - self.ROCKET.STAGES[1].PROPELLANT_MASS
            self.DV2 = self.ROCKET.STAGES[1].ISP*g0*np.log(self.MASS_INITIAL_2/self.MASS_FINAL_2)

        if len(self.ROCKET.STAGES)>2:
            self.MASS_INITIAL_2 = self.MASS_INITIAL_1 - self.ROCKET.STAGES[0].TOTAL_MASS
            self.MASS_FINAL_2 = self.MASS_INITIAL_2 - self.ROCKET.STAGES[1].PROPELLANT_MASS
            self.DV2 = self.ROCKET.STAGES[1].ISP*g0*np.log(self.MASS_INITIAL_2/self.MASS_FINAL_2)
            self.MASS_INITIAL_3 = self.MASS_INITIAL_2 - self.ROCKET.STAGES[1].TOTAL_MASS - self.ROCKET.FAIRING_MASS
            self.MASS_FINAL_3 = self.MASS_INITIAL_3 - self.ROCKET.STAGES[2].PROPELLANT_MASS
            self.DV3 = self.ROCKET.STAGES[2].ISP*g0*np.log(self.MASS_INITIAL_3/self.MASS_FINAL_3)

        self.DV = self.DV1 + self.DV2 + self.DV3
        self.LOSSES = 2.452e-3*self.ALTITUDE**2 + 1.051*self.ALTITUDE+1387.5
        self.V_INITIAL = Omega_e*R_e*np.cos(np.deg2rad(self.LATITUDE))*np.sin(np.deg2rad(self.AZIMUTH))/86.4
        self.V_FINAL = self.V_INITIAL + self.DV - self.LOSSES
        self.VF = np.sqrt(GM_e/self.PERIGEE)*1000
        self.DV_REQUIRED = self.VF - self.V_INITIAL + self.LOSSES

        if len(self.ROCKET.STAGES)==2:
            k_1 = self.ROCKET.STAGES[0].STRUCTURAL_INDEX
            k_2 = self.ROCKET.STAGES[1].STRUCTURAL_INDEX
            k_3 = 1

            W_1 = k_1/(1+k_1)
            W_2 = k_2/(1+k_2)
            W_3 = k_3/(1+k_3)

            ISP1 = self.ROCKET.STAGES[0].ISP
            ISP2 = self.ROCKET.STAGES[1].ISP

            b2 = b_last
            b1 = (1/W_1)*(1-(ISP2/ISP1)*(1-W_2*b2))
            DeltaV_r=g0*ISP1*np.log(b1)+g0*ISP2*np.log(b2)
            h_list=[]
            h=pas
            sign_0=1
            while np.abs(self.DV_REQUIRED-DeltaV_r)>error_min:
                DeltaV_r =g0*ISP1*np.log(b1)+g0*ISP2*np.log(b2)
                b1 = (1/W_1)*(1-(ISP2/ISP1)*(1-W_2*b2))
                old_b2 = b2
                if self.DV_REQUIRED>DeltaV_r:
                    b2+=h
                else :
                    b2-=h
                sign_1=old_b2-b2
                if np.sign(sign_0) != np.sign(sign_1):
                    h=h*0.8
                h_list.append(h)
                if b1<=0 or b2<=0:
                    self.message="diverged"
                    break
            a1 = ((1+k_1)/b1) - k_1
            a2 = ((1+k_2)/b2) - k_2
            Mi1 = (self.ROCKET.PAYLOAD_MASS / a2) / a1
            Mi2 = self.ROCKET.PAYLOAD_MASS / a2
            me1 = Mi1*(1-a1)/(1+k_1)
            ms1 = (me1*k_1)
            me2 = Mi2*(1-a2)/(1+k_2)
            ms2 = (me2*k_2)
            me3 = 0
            ms3 = 0
            
                
        if len(self.ROCKET.STAGES)==3:
            
            k_1 = self.ROCKET.STAGES[0].STRUCTURAL_INDEX
            k_2 = self.ROCKET.STAGES[1].STRUCTURAL_INDEX
            k_3 = self.ROCKET.STAGES[2].STRUCTURAL_INDEX

            W_1 = k_1/(1+k_1)
            W_2 = k_2/(1+k_2)
            W_3 = k_3/(1+k_3)

            ISP1 = self.ROCKET.STAGES[0].ISP
            ISP2 = self.ROCKET.STAGES[1].ISP
            ISP3 = self.ROCKET.STAGES[2].ISP

            b3 = b_last
            b2 = (1/W_2)*(1-(ISP3/ISP2)*(1-W_3*b3))
            b1 = (1/W_1)*(1-(ISP2/ISP1)*(1-W_2*b2))

            DeltaV_r = g0*ISP1*np.log(b1)+g0*ISP2*np.log(b2)+g0*ISP3*np.log(b3)
            h_list=[]
            h=pas
            sign_0=1
            while np.abs(self.DV_REQUIRED-DeltaV_r)>error_min:
                DeltaV_r = g0*ISP1*np.log(b1)+g0*ISP2*np.log(b2)+g0*ISP3*np.log(b3)

                b2 = (1/W_2)*(1-(ISP3/ISP2)*(1-W_3*b3))
                b1 = (1/W_1)*(1-(ISP2/ISP1)*(1-W_2*b2))

                old_b3 = b3
                if self.DV_REQUIRED>DeltaV_r:
                    b3+=h
                else :
                    b3-=h
                sign_1=old_b3-b3
                if np.sign(sign_0) != np.sign(sign_1):
                    h=h*0.8
                h_list.append(h)
                if b1<=0 or b2<=0 or b3<=0:
                    self.message="diverged"
                    break
            a1 = ((1+k_1)/b1) - k_1
            a2 = ((1+k_2)/b2) - k_2
            a3 = ((1+k_3)/b3) - k_3
            Mi1 = ((self.ROCKET.PAYLOAD_MASS / a3) / a2)/ a1
            Mi2 = (self.ROCKET.PAYLOAD_MASS / a3) / a2
            Mi3 = self.ROCKET.PAYLOAD_MASS / a3
            me1 = Mi1*(1-a1)/(1+k_1)
            ms1 = (me1*k_1)
            me2 = Mi2*(1-a2)/(1+k_2)
            ms2 = (me2*k_2)
            me3 = Mi3*(1-a3)/(1+k_3)
            ms3 = (me3*k_3)
            
        if me1+ms1+me2+ms2+me3+ms3+self.ROCKET.PAYLOAD_MASS<1000000:
            if me1+ms1 > me2+ms2+me3+ms3+self.ROCKET.PAYLOAD_MASS:
                if me2+ms2 > me3+ms3+self.ROCKET.PAYLOAD_MASS:
                    
                    self.me1 = np.around(me1,3)
                    self.ms1 = np.around(ms1,3)
                    self.me2 = np.around(me2,3)
                    self.ms2 = np.around(ms2,3)
                    self.me3 = np.around(me3,3)
                    self.ms3 = np.around(ms3,3)
                    self.m_total = np.around(me1+ms1+me2+ms2+me3+ms3,3)

                    if 500<ms1 and ms1<100000:
                        self.message = "mission allowed"
                    else:
                        self.message = "crit mass s1"

                    if 200<ms2 and ms2<80000:
                        self.message = "mission allowed"
                    else:
                        self.message = "crit mass s2"   
                    
                    if len(self.ROCKET.STAGES)==3:
                        if 200<ms3 and ms3<50000:
                            self.message = "mission allowed"
                        else:
                            self.message = "crit mass s3"

                        
                    

        else:
            self.message = "error"


        self.SEMI_MAJOR_AXIS = 1/((2/self.PERIGEE) - ((self.V_FINAL/1000)**2/GM_e))
        self.ECCENTRICITY = np.abs(1-(self.PERIGEE/self.SEMI_MAJOR_AXIS))
        self.APOGEE = self.SEMI_MAJOR_AXIS*(1+self.ECCENTRICITY)
        self.PERIGEE = self.SEMI_MAJOR_AXIS*(1-self.ECCENTRICITY)

