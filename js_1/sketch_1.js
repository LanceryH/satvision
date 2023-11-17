let satellite_val = 0;
let my_object;
let data_sat;
let val_py;
let date_py;
let live_statut;

function preload() {
  data_sat = loadJSON("../data.json");
  data_py = loadJSON("../param.json");
  img = loadImage("map_earth.jpg");
}

function setup() {
  createCanvas(501, 384, WEBGL);
  //resizeCanvas(windowWidth, windowHeight);
  val_py = data_py[0]["val"];
  date_py = data_py[0]["date"];
  live_statut = data_py[0]["live"];
  my_object = new Orbit(data_sat[val_py], date_py, live_statut);
  my_object.total();
  angleMode(DEGREES);
}

function draw() {
  my_object = new Orbit(data_sat[val_py], date_py, live_statut);
  my_object.total();

  clear();
  orbitControl(1, 1, 1);
  scale(0.02);

  push();
  fill(0, 100, 100);
  texture(img);
  rotateX(0);
  rotateY(-180);
  rotateZ(0);
  sphere(6371, 25, 25);
  pop();

  push();
  stroke(255, 0, 255);
  strokeWeight(3);
  beginShape(POINTS);
  for (let index = 0; index < my_object.R[0].length; index++) {
    vertex(
      (Math.cos((my_object.lat[index] * Math.PI) / 180) *
        Math.sin((my_object.lon[index] * Math.PI) / 180) *
        my_object.alt[index]) /
        1000,
      (-Math.sin((my_object.lat[index] * Math.PI) / 180) * my_object.alt[0]) /
        1000,
      (Math.cos((my_object.lat[index] * Math.PI) / 180) *
        Math.cos((my_object.lon[index] * Math.PI) / 180) *
        my_object.alt[index]) /
        1000
    );
  }
  endShape();
  pop();

  push();
  stroke(0, 255, 0);
  strokeWeight(10);
  beginShape(POINTS);
  vertex(
    (Math.cos((my_object.lat[0] * Math.PI) / 180) *
      Math.sin((my_object.lon[0] * Math.PI) / 180) *
      my_object.alt[0]) /
      1000,
    (-Math.sin((my_object.lat[0] * Math.PI) / 180) * my_object.alt[0]) / 1000,
    (Math.cos((my_object.lat[0] * Math.PI) / 180) *
      Math.cos((my_object.lon[0] * Math.PI) / 180) *
      my_object.alt[0]) /
      1000
  );
  endShape();
  pop();
  push();
  strokeWeight(3);
  stroke(0, 0, 255); //BLUE
  line(0, 0, 0, 0, 10000, 0);
  stroke(255, 0, 0); //RED
  line(0, 0, 0, 0, -10000, 0);
}
