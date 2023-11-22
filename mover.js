class Orbit {
  constructor(data, date_py, live_statut, Dt_py) {
    this.Dt_py = Dt_py;
    this.live_statut = live_statut;
    this.Dt_py_YEAR = parseInt(Dt_py[0]);
    this.Dt_py_MONTH = parseInt(Dt_py[1]);
    this.Dt_py_DAY = parseInt(Dt_py[2]);
    this.Dt_py_HOUR = parseInt(Dt_py[3]);
    this.Dt_py_MINUTE = parseInt(Dt_py[4]);
    this.Dt_py_SECOND = 0;
    this.date_py_YEAR = parseInt(date_py[0]);
    this.date_py_MONTH = parseInt(date_py[1]);
    this.date_py_DAY = parseInt(date_py[2]);
    this.date_py_HOUR = parseInt(date_py[3]);
    this.date_py_MINUTE = parseInt(date_py[4]);
    this.date_py_SECOND = 0;
    this.MUE = 398600.441;
    this.EARTH_MASS = 5.972e24;
    this.G = 6.67384e-11;
    this.NAME = data.OBJECT_NAME;
    this.NORA_ID = data.OBJECT_ID;
    this.EPOCH = data.EPOCH;
    this.MEAN_MOTION = data.MEAN_MOTION;
    this.ECCENTRICITY = (data.ECCENTRICITY * Math.PI) / 180;
    this.INCLINATION = (data.INCLINATION * Math.PI) / 180;
    this.RA_OF_ASC_NODE = (data.RA_OF_ASC_NODE * Math.PI) / 180;
    this.ARG_OF_PERICENTER = (data.ARG_OF_PERICENTER * Math.PI) / 180;
    this.MEAN_ANOMALY = (data.MEAN_ANOMALY * Math.PI) / 180;
    this.UPDATE_DATE_YEAR = undefined;
    this.UPDATE_DATE_MONTH = undefined;
    this.UPDATE_DATE_DAY = undefined;
    this.UPDATE_DATE_HOUR = undefined;
    this.UPDATE_DATE_MINUTE = undefined;
    this.UPDATE_DATE_SECOND = undefined;
    this.EPOCH_NOW = undefined;
    this.PERIOD = (1 / this.MEAN_MOTION) * 24 * 60 * 60;
    this.ARGUMENT_OF_PERIAPSIS = this.ARG_OF_PERICENTER - this.RA_OF_ASC_NODE;
    this.MEAN_ANOMALY_UPDATED = undefined;
    this.SEMI_MAJOR_AXIS = undefined;
    this.ECCENTRIC_ANOMALY = undefined;
    this.GMST = undefined;
    this.R = undefined;
    this.Rdot = undefined;
    this.lon = undefined;
    this.lat = undefined;
    this.alt = undefined;
  }

  create_date_data() {
    const str = this.EPOCH || "";
    this.UPDATE_DATE_YEAR = parseInt(this.EPOCH?.slice(0, 4));
    this.UPDATE_DATE_MONTH = parseInt(this.EPOCH?.slice(5, 7));
    this.UPDATE_DATE_DAY = parseInt(this.EPOCH?.slice(8, 10));
    this.UPDATE_DATE_HOUR = parseInt(this.EPOCH?.slice(11, 13));
    this.UPDATE_DATE_MINUTE = parseInt(this.EPOCH?.slice(14, 16));
    this.UPDATE_DATE_SECOND = parseInt(this.EPOCH?.slice(17, 19));
  }

  matrixMult(a, b) {
    var aNumRows = a.length,
      aNumCols = a[0].length,
      bNumCols = b[0].length,
      m = new Array(aNumRows); // initialize array of rows
    for (var r = 0; r < aNumRows; ++r) {
      m[r] = new Array(bNumCols); // initialize the current row
      for (var c = 0; c < bNumCols; ++c) {
        m[r][c] = 0; // initialize the current cell
        for (var i = 0; i < aNumCols; ++i) {
          m[r][c] += a[r][i] * b[i][c];
        }
      }
    }
    return m;
  }

  create_arrange(start, stop, step) {
    step = step || 1;
    var arr = [];
    for (var i = start; i < stop; i += step) {
      arr.push(i);
    }
    return arr;
  }

  create_array(size, value) {
    var arr = [];
    for (var i = 0; i < size; i += 1) {
      arr.push(value);
    }
    return arr;
  }

  meanMotion() {
    return Math.sqrt(
      (this.EARTH_MASS * this.G) / Math.pow(this.SEMI_MAJOR_AXIS, 3)
    );
  }

  meanAnomaly(t) {
    return this.MEAN_ANOMALY + this.MEAN_MOTION * t;
  }

  eccentricAnomaly() {
    // https://fr.wikipedia.org/wiki/%C3%89quation_de_Kepler
    const epsilon = 1e-3;
    let convergence = 1;
    let ECCENTRIC_ANOMALY_N = this.MEAN_ANOMALY_UPDATED;

    while (convergence > epsilon) {
      let numerator =
        ECCENTRIC_ANOMALY_N -
        this.ECCENTRICITY * Math.sin(ECCENTRIC_ANOMALY_N) -
        this.MEAN_ANOMALY_UPDATED;
      let denominator = 1 - this.ECCENTRICITY * Math.cos(ECCENTRIC_ANOMALY_N);
      let ECCENTRIC_ANOMALY_N1 = ECCENTRIC_ANOMALY_N + numerator / denominator;
      convergence = Math.abs(ECCENTRIC_ANOMALY_N1 - ECCENTRIC_ANOMALY_N);
      ECCENTRIC_ANOMALY_N = ECCENTRIC_ANOMALY_N1;
    }

    return ECCENTRIC_ANOMALY_N;
  }

  matrixOfTransition() {
    // Géocentrique équatorial -> Repère orbital tournant
    // https://hal.science/tel-03078743/document (p56)

    const M1 = [
      [Math.cos(-this.ARG_OF_PERICENTER), Math.sin(-this.ARG_OF_PERICENTER), 0],
      [
        -Math.sin(-this.ARG_OF_PERICENTER),
        Math.cos(-this.ARG_OF_PERICENTER),
        0,
      ],
      [0, 0, 1],
    ];

    const M2 = [
      [1, 0, 0],
      [0, Math.cos(-this.INCLINATION), Math.sin(-this.INCLINATION)],
      [0, -Math.sin(-this.INCLINATION), Math.cos(-this.INCLINATION)],
    ];

    const M3 = [
      [Math.cos(-this.RA_OF_ASC_NODE), Math.sin(-this.RA_OF_ASC_NODE), 0],
      [-Math.sin(-this.RA_OF_ASC_NODE), Math.cos(-this.RA_OF_ASC_NODE), 0],
      [0, 0, 1],
    ];

    return this.matrixMult(this.matrixMult(M3, M2), M1);
  }

  conversionToCartesian(t) {
    this.MEAN_MOTION = this.meanMotion();
    this.MEAN_ANOMALY_UPDATED = this.meanAnomaly(t);
    this.ECCENTRIC_ANOMALY = this.eccentricAnomaly();

    // Calculate the satellite's coordinates in the perifocal frame
    const r =
      this.SEMI_MAJOR_AXIS *
      (1 - this.ECCENTRICITY * Math.cos(this.ECCENTRIC_ANOMALY));
    const x =
      this.SEMI_MAJOR_AXIS *
      (Math.cos(this.ECCENTRIC_ANOMALY) - this.ECCENTRICITY);
    const y =
      this.SEMI_MAJOR_AXIS *
      Math.sqrt(1 - this.ECCENTRICITY ** 2) *
      Math.sin(this.ECCENTRIC_ANOMALY);
    const z = 0;

    const xDot =
      (-Math.sin(this.ECCENTRIC_ANOMALY) *
        this.MEAN_MOTION *
        this.SEMI_MAJOR_AXIS ** 2) /
      r;
    const yDot =
      (Math.sqrt(1 - this.ECCENTRICITY ** 2) *
        Math.cos(this.ECCENTRIC_ANOMALY) *
        this.MEAN_MOTION *
        this.SEMI_MAJOR_AXIS ** 2) /
      r;
    const zDot = 0;

    const posMatrix = this.matrixMult(this.matrixOfTransition(), [
      [x],
      [y],
      [z],
    ]);
    const vitMatrix = this.matrixMult(this.matrixOfTransition(), [
      [xDot],
      [yDot],
      [zDot],
    ]);

    const fiEarth = (t * 2 * Math.PI * (1 + 1 / 365.25)) / (3600 * 24);
    const rotMatrix = [
      [Math.cos(fiEarth), Math.sin(fiEarth), 0],
      [-Math.sin(fiEarth), Math.cos(fiEarth), 0],
      [0, 0, 1],
    ];

    const posResult = this.matrixMult(rotMatrix, posMatrix);
    const vitResult = this.matrixMult(rotMatrix, vitMatrix);

    return [posResult, vitResult];
  }

  calculate_GMST(year, month, day, hour, minute, second) {
    // Calculate the Julian Date (JD) for the given date and time
    const a = Math.floor((14 - month) / 12);
    const y = year + 4800 - a;
    const m = month + 12 * a - 3;
    let JD =
      day +
      Math.floor((153 * m + 2) / 5) +
      365 * y +
      Math.floor(y / 4) -
      Math.floor(y / 100) +
      Math.floor(y / 400) -
      32045;
    JD += (hour - 12) / 24.0 + minute / 1440.0 + second / 86400.0;

    // Calculate the Julian centuries since J2000.0
    const T = (JD - 2451545.0) / 36525.0;

    // Calculate the mean sidereal time in degrees
    this.GMST =
      280.46061837 +
      360.98564736629 * (JD - 2451545.0) +
      T ** 2 * (0.000387933 - T / 38710000);

    // Ensure the result is in the range [0, 360] degrees
    this.GMST %= 360;

    return this.GMST;
  }

  conversionToGeodic() {
    let GMST = this.calculate_GMST(
      this.UPDATE_DATE_YEAR,
      this.UPDATE_DATE_MONTH,
      this.UPDATE_DATE_DAY,
      this.UPDATE_DATE_HOUR,
      this.UPDATE_DATE_MINUTE,
      this.UPDATE_DATE_SECOND
    );
    const x = this.R[0];
    const y = this.R[1];
    const z = this.R[2];
    this.alt = this.create_array(this.R[0].length, 0);
    this.lon = this.create_array(this.R[0].length, 0);
    this.lat = this.create_array(this.R[0].length, 0);

    for (let j = 0; j < this.R[0].length; j++) {
      this.alt[j] = Math.sqrt(x[j] * x[j] + y[j] * y[j] + z[j] * z[j]);
    }

    for (let j = 0; j < this.R[0].length; j++) {
      this.lon[j] = (180 / Math.PI) * Math.atan2(y[j], x[j]) - GMST;

      if (this.lon[j] > 180) {
        this.lon[j] = this.lon[j] - 360;
      } else if (this.lon[j] < -180) {
        this.lon[j] = this.lon[j] + 360;
      }

      this.lat[j] = Math.asin(z[j] / this.alt[j]);
      let a = 6378137;
      let b = 6356752.314235;
      let f = (a - b) / a;

      this.lat[j] =
        (180 / Math.PI) * Math.atan(Math.tan(this.lat[j]) * (1 - f * f));
      //lat = np.rad2deg(np.arctan(np.tan(lat)*(1-f**2)))
      //lat = (np.arcsin(z/p))
      //this.lat[j] = (180 / Math.PI) * Math.atan(Math.tan());
    }
    return [this.lon, this.lat];
  }

  total() {
    this.create_date_data();
    let nbOrbit = 0;
    let d2 = 0;
    if (this.live_statut == 0) {
      d2 = new Date(
        this.date_py_YEAR,
        this.date_py_MONTH,
        this.date_py_DAY,
        this.date_py_HOUR,
        this.date_py_MINUTE,
        this.date_py_SECOND
      );
    }
    if (this.live_statut == 2) {
      d2 = new Date();
    }
    const dt_python = new Date(
      this.Dt_py_YEAR,
      this.Dt_py_MONTH,
      this.Dt_py_DAY,
      this.Dt_py_HOUR,
      this.Dt_py_MINUTE,
      this.Dt_py_SECOND
    );
    const d1 = new Date(
      this.UPDATE_DATE_YEAR,
      this.UPDATE_DATE_MONTH - 1,
      this.UPDATE_DATE_DAY,
      this.UPDATE_DATE_HOUR,
      this.UPDATE_DATE_MINUTE,
      this.UPDATE_DATE_SECOND
    );
    if (this.live_statut == 2) {
      nbOrbit = 1;
    }
    if (this.live_statut == 0) {
      nbOrbit = (dt_python - d2) / 1000 / this.PERIOD;
    }
    this.MEAN_MOTION_SI = (2 * Math.PI) / this.PERIOD;
    this.SEMI_MAJOR_AXIS =
      Math.pow(this.MUE / this.MEAN_MOTION_SI ** 2, 1 / 3) * 1000;

    const nbIts = parseInt(nbOrbit * this.PERIOD);
    const nbPts = parseInt(nbOrbit * 50);
    const T = this.create_arrange(0, parseInt(nbIts), parseInt(nbIts / nbPts));
    this.EPOCH_NOW = d2;
    const dt = (d2 - d1) / 1000 - 3600; //FAUT METTRE LA CORRECTION DU GMT+00

    this.R = [
      this.create_array(0, nbPts),
      this.create_array(0, nbPts),
      this.create_array(0, nbPts),
    ];
    this.Rdot = [
      this.create_array(0, nbPts),
      this.create_array(0, nbPts),
      this.create_array(0, nbPts),
    ];

    for (let j = 0; j < nbPts; j++) {
      const [pos, vit] = this.conversionToCartesian(T[j] + dt);
      this.R[0][j] = pos[0];
      this.R[1][j] = pos[1];
      this.R[2][j] = pos[2];
      this.Rdot[0][j] = vit[0];
      this.Rdot[1][j] = vit[1];
      this.Rdot[2][j] = vit[2];
    }

    this.conversionToGeodic();
    return this.R;
  }
}
