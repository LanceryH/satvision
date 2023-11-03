let satellite_val = 0;
let my_object;
let data_sat;

function preload() {
  data_sat = loadJSON("data.json");
  img = loadImage("map_earth.jpg");
}

function setup() {
  let canvas = createCanvas(windowWidth, windowHeight, WEBGL);
  canvas.position(0, 0);
  sel = createSelect();
  sel.id(12);
  for (let index = 0; index < 100; index++) {
    sel.option(index + ": " + data_sat[index].OBJECT_NAME);
    sel.changed(mySelectEvent_listbox);
  }
  my_object = new Orbit(data_sat[0]);
  my_object.total();
  angleMode(DEGREES);
}

function mySelectEvent_listbox() {
  let item = sel.selected();
  let val = 0;
  for (let index = 0; index < item.length; index++) {
    if (item[index] == ":") {
      val = parseInt(item.slice(0, index));
    }
  }
  satellite_val = val;
  my_object = new Orbit(data_sat[satellite_val]);
}

function draw() {
  my_object = new Orbit(data_sat[satellite_val]);
  my_object.total();

  clear();
  orbitControl(1, 1, 1);
  scale(0.03);

  push();
  fill(0, 100, 100);
  texture(img);
  rotateX(0);
  rotateY(-180);
  rotateZ(0);
  sphere(6371, 50, 50);
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

  document.getElementById("text_parameters").innerHTML =
    "Period: " +
    round(my_object.PERIOD, 2) +
    " min <br />Latitude: " +
    round(my_object.lat[0], 2) +
    "° <br />Longitude: " +
    round(my_object.lon[0], 2) +
    " ° <br />Epoch: " +
    my_object.EPOCH +
    "<br />GMST: " +
    round(my_object.GMST) +
    " °<br />Inclination: " +
    round((my_object.INCLINATION * 180) / Math.PI, 2) +
    " °";

  let canvas = document.getElementById("plot_groundtrack");
  let ctx = canvas.getContext("2d");
  ctx.beginPath();
  ctx.clearRect(0, 0, 360, 180);
  ctx.closePath();

  ctx.fillStyle = "#ff00ff";
  ctx.beginPath();
  for (let index = 0; index < my_object.R[0].length; index++) {
    ctx.fillRect(my_object.lon[index] + 180, 90 - my_object.lat[index], 1, 1);
  }
  ctx.closePath();

  ctx.beginPath();
  ctx.arc(my_object.lon[0] + 180, 90 - my_object.lat[0], 4, 0, Math.PI * 2);
  ctx.fillStyle = "#00ff00";
  ctx.fill();
  ctx.closePath();
  console.log(sel.id());
}
