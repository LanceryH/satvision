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
  img = loadImage("../map_earth.jpg");
  img_moon = loadImage("../map_moon.jpg");
}

function setup() {
  cnv = createCanvas(windowWidth, windowHeight, WEBGL);
  cnv.position(0, 0, "fixed");
  //resizeCanvas(windowWidth, windowHeight);
  val_py = data_py["val"];
  date_py = data_py["date"];
  live_statut = data_py["live"];
  Dt_py = data_py["Dt"];
  my_object = new Orbit(data_sat[val_py], date_py, live_statut, Dt_py);
  angleMode(DEGREES);
}

function draw() {
  my_object.total();

  clear();
  orbitControl(1, 1, 1);
  scale(0.02);
  perspective(180 / 3.0, width / height, 0.1, 150000);
  //pointLight(255, 255, 255, 15000, 15000, 15000);

  push();
  texture(img);
  rotateX(0);
  rotateY(-180);
  rotateZ(0);
  sphere(6371, 25, 25);
  pop();

  push();
  texture(img_moon);
  rotateX(0);
  rotateY(-180);
  rotateZ(0);
  translate(384400, 0);
  sphere(1737, 25, 25);
  pop();

  push();
  noFill();
  stroke(255, 255, 0);
  strokeWeight(1);
  for (let index = 0; index < 50; index++) {
    rotateY(15);
    ellipse(0, 0, 6375 * 2, 6375 * 2, 50);
  }
  pop();

  push();
  stroke(255, 0, 255);
  strokeWeight(2);
  noFill();
  beginShape();
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
  stroke(0, 255, 255);
  strokeWeight(10);
  beginShape(POINTS);
  const max_len = my_object.lat.length - 1;
  vertex(
    (Math.cos((my_object.lat[max_len] * Math.PI) / 180) *
      Math.sin((my_object.lon[max_len] * Math.PI) / 180) *
      my_object.alt[0]) /
      1000,
    (-Math.sin((my_object.lat[max_len] * Math.PI) / 180) * my_object.alt[0]) /
      1000,
    (Math.cos((my_object.lat[max_len] * Math.PI) / 180) *
      Math.cos((my_object.lon[max_len] * Math.PI) / 180) *
      my_object.alt[max_len]) /
      1000
  );
  endShape();
  pop();

  //push();
  //strokeWeight(3);
  //stroke(0, 0, 255); //BLUE
  //line(0, 0, 0, 0, 10000, 0);
  //stroke(255, 0, 0); //RED
  //line(0, 0, 0, 0, -10000, 0);
}
