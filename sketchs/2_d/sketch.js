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

  for (let index_1 = 0; index_1 < data_py[0]["val"].length; index_1++) {
    my_object = new Orbit(
      data_sat[val_py[index_1]],
      date_py,
      live_statut,
      Dt_py
    );
    my_object.total();

    let line_right_lon = [];
    let line_right_lat = [];
    let line_left_lon = [];
    let line_left_lat = [];

    index_left = 0;

    for (let index = 0; index < my_object.lat.length; index++) {
      if (
        my_object.lon[0] <= my_object.lon[index] &&
        my_object.lon[index] < 180
      ) {
        line_right_lon.push(my_object.lon[index]);
        line_right_lat.push(-my_object.lat[index]);
      } else {
        index_left = index;
        break;
      }
    }

    for (let index = index_left; index < my_object.lon.length; index++) {
      line_left_lon.push(my_object.lon[index]);
      line_left_lat.push(-my_object.lat[index]);
    }

    push();
    stroke(color[index_1][0], color[index_1][1], color[index_1][2]);
    strokeWeight(2);
    noFill();
    beginShape();
    for (let index = 0; index < line_right_lon.length; index++) {
      vertex(line_right_lon[index], line_right_lat[index]);
    }
    endShape();
    pop();

    push();
    stroke(color[index_1][0], color[index_1][1], color[index_1][2]);
    strokeWeight(2);
    noFill();
    beginShape();
    for (let index = 0; index < line_left_lon.length; index++) {
      vertex(line_left_lon[index], line_left_lat[index]);
    }
    endShape();
    pop();

    push();
    stroke(0, 210, 106);
    strokeWeight(10);
    beginShape(POINTS);
    vertex(my_object.lon[0], -my_object.lat[0]);
    endShape();
    pop();

    push();
    const max_len = my_object.lat.length - 1;
    stroke(0, 116, 186);
    strokeWeight(10);
    beginShape(POINTS);
    vertex(my_object.lon[max_len], -my_object.lat[max_len]);
    endShape();
    pop();
    noFill();
  }

  beginShape();
  vertex(-180, -90);
  vertex(180, -90);
  vertex(180, 90);
  vertex(-180, 90);
  endShape(CLOSE);
}
