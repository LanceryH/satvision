let satellite_val = 0;
let my_object;
let data_sat;
let val_py;

function preload() {
  data_sat = loadJSON("../data.json");
  data_py = loadJSON("../param.json");
  img = loadImage("map_earth.jpg");
}

function setup() {
  createCanvas(501, 184, WEBGL);
  background(255);
  //resizeCanvas(windowWidth, windowHeight);
  val_py = data_py[0]["val"];
  my_object = new Orbit(data_sat[val_py]);
  my_object.total();
  angleMode(DEGREES);
}

function draw() {
  background(255);
  my_object = new Orbit(data_sat[val_py]);
  my_object.total();
  scale(1.0);
  push();
  texture(img);
  rect(-180, -90, 360, 180);
  pop();
}
