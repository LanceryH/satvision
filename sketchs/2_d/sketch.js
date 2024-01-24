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
  img = loadImage("../../image/map_earth_nocloud.jpg");
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
  orbitControl(0, 0, 0);
  scale(1.5);
  clear();
  background(250, 250, 250);
  push();
  stroke(240, 240, 240);
  texture(img);
  rect(-180, -90, 360, 180);
  pop();

  for (let index = 0; index < data_py[0]["val"].length; index++) {
    my_object = new Orbit(data_sat[val_py[index]], date_py, live_statut, Dt_py);
    my_object.total();

    push();
    stroke(color[0], color[1], color[2]);
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
}
