let satellite_val = 0;
let my_object;
let data_sat;
let val_py;
let date_py;
let live_statut;
let Dt_py;

function preload() {
  data_sat = loadJSON("../data.json");
  data_py = loadJSON("../param.json");
}

function setup() {
  let canvas = createCanvas(100, 100);
  canvas.position(0, 0);
  //resizeCanvas(windowWidth, windowHeight);
  val_py = data_py[0]["val"];
  date_py = data_py[0]["date"];
  live_statut = data_py[0]["live"];
  Dt_py = data_py[0]["Dt"];
  my_object = new Orbit(data_sat[val_py], date_py, live_statut, Dt_py);
  my_object.total();
}

function draw() {
  my_object = new Orbit(data_sat[val_py], date_py, live_statut, Dt_py);
  my_object.total();

  document.getElementById("param").innerHTML =
    "Period: " +
    round(my_object.PERIOD, 2) +
    " min " +
    "<br />Latitude: " +
    round(my_object.lat[0], 2) +
    "° " +
    "<br />Longitude: " +
    round(my_object.lon[0], 2) +
    "° " +
    "<br />Inclination: " +
    round((my_object.INCLINATION * 180) / Math.PI, 2) +
    " °" +
    "<br />NORA ID: " +
    my_object.NORA_ID +
    "<br />GMST: " +
    my_object.GMST +
    "<br />Altitude: " +
    round(my_object.alt[0], 2) +
    " Km";
}
