let satellite_val = 0;
let my_object;
let data_sat;
let val_py;
let date_py;
let live_statut;
let Dt_py;

function preload() {
  data_sat = loadJSON("../../jsons/data.json");
  data_py = loadJSON("../../jsons/param.json");
  img = loadImage("../../image/map_earth.jpg");
  img_moon = loadImage("../../image/map_moon.jpg");
}

function setup() {
  cnv = createCanvas(windowWidth, windowHeight, WEBGL);
  cnv.position(0, 0, "fixed");

  val_py = data_py[0]["val"];
  date_py = data_py[0]["date"];
  live_statut = data_py[0]["live"];
  Dt_py = data_py[0]["Dt"];
  color = data_py[0]["color"];
  for (let index = 0; index < data_py[0]["val"].length; index++) {
    my_object = new Orbit(data_sat[val_py[index]], date_py, live_statut, Dt_py);
    my_object.total();
  }
  angleMode(DEGREES);
}

function draw() {
  clear();
  background(0);
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

  for (let index_1 = 0; index_1 < data_py[0]["val"].length; index_1++) {
    my_object = new Orbit(
      data_sat[val_py[index_1]],
      date_py,
      live_statut,
      Dt_py
    );
    my_object.total();

    push();
    stroke(color[index_1][0], color[index_1][1], color[index_1][2]);
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
    stroke(0, 210, 106);
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
    stroke(0, 116, 186);
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
  }
}
