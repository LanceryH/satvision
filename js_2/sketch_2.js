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
  img = loadImage("../map_earth_nocloud.jpg");
}

function setup() {
  createCanvas(501, 184, WEBGL);
  background(255);
  //resizeCanvas(windowWidth, windowHeight);
  val_py = data_py["val"];
  date_py = data_py["date"];
  live_statut = data_py["live"];
  Dt_py = data_py["Dt"];
  my_object = new Orbit(data_sat[val_py], date_py, live_statut, Dt_py);
  angleMode(DEGREES);
}

function draw() {
  background(249, 249, 249);
  my_object.total();

  orbitControl(0, 0, 1);
  scale(1.0);

  push();
  stroke(240, 240, 240);
  texture(img);
  rect(-180, -90, 360, 180);
  pop();

  push();
  stroke(255, 0, 255);
  strokeWeight(3);
  beginShape(POINTS);
  for (let index = 0; index < my_object.lat.length; index++) {
    vertex(my_object.lon[index], -my_object.lat[index]);
  }
  endShape();
  pop();

  push();
  stroke(0, 255, 0);
  strokeWeight(10);
  beginShape(POINTS);
  vertex(my_object.lon[0], -my_object.lat[0]);
  endShape();
  pop();

  push();
  const max_len = my_object.lat.length - 1;
  stroke(0, 255, 255);
  strokeWeight(10);
  beginShape(POINTS);
  vertex(my_object.lon[max_len], -my_object.lat[max_len]);
  endShape();
  pop();
}
