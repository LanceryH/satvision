let satellite_val = 0;
let my_object;
let data_sat;
let val_py;

function preload() {
  data_sat = loadJSON("../data.json");
  data_py = loadJSON("../param.json");
}

function setup() {
  let canvas = createCanvas(100, 100);
  canvas.position(0, 0);
  //resizeCanvas(windowWidth, windowHeight);
  val_py = data_py[0]["val"];
  my_object = new Orbit(data_sat[val_py]);
  my_object.total();
}

function draw() {
  my_object = new Orbit(data_sat[val_py]);
  my_object.total();

  document.getElementById("param").innerHTML =
    "Period: " +
    round(my_object.PERIOD, 2) +
    " min <br />Latitude: " +
    round(my_object.lat[0], 2) +
    "° <br />Longitude: " +
    round(my_object.lon[0], 2) +
    "<br />Inclination: " +
    round((my_object.INCLINATION * 180) / Math.PI, 2) +
    " °";
}
