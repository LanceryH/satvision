let satellite_val = 0;
let my_object;
let data_sat;

var s3 = function (sketch) {
  sketch.preload = function () {
    data_sat = sketch.loadJSON("data.json");
    img = sketch.loadImage("map_earth.jpg");
  };
  sketch.setup = function () {
    let canvas = sketch.createCanvas(
      sketch.windowWidth - (360 + sketch.windowWidth * 0.01),
      sketch.windowHeight,
      sketch.WEBGL
    );
    canvas.position(360 + sketch.windowWidth * 0.01, 0);
    sel = sketch.createSelect();
    for (let index = 0; index < 100; index++) {
      sel.position(20, 20);
      sel.option(index + ":" + data_sat[index].OBJECT_NAME);
      sel.changed(mySelectEvent_listbox);
    }
    my_object = new Orbit(data_sat[0]);
    my_object.total();
  };

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

  sketch.draw = function () {
    my_object = new Orbit(data_sat[satellite_val]);
    my_object.total();

    sketch.clear();
    sketch.orbitControl(1, 1, 1);
    sketch.scale(0.03);

    sketch.push();
    sketch.fill(0, 100, 100);
    sketch.texture(img);
    sketch.rotateX(0);
    sketch.rotateY(((180 + my_object.lon[0]) * Math.PI) / 180);
    sketch.rotateZ(0);
    sketch.sphere(6371, 50, 50);
    sketch.pop();

    sketch.push();
    sketch.stroke(255, 0, 255);
    sketch.strokeWeight(3);
    sketch.beginShape(sketch.POINTS);
    for (let index = 0; index < my_object.R[0].length; index++) {
      sketch.vertex(
        -my_object.R[0][index] / 1000,
        -my_object.R[2][index] / 1000,
        my_object.R[1][index] / 1000
      );
    }
    sketch.endShape();
    sketch.pop();

    sketch.push();
    sketch.stroke(0, 255, 0);
    sketch.strokeWeight(10);
    sketch.beginShape(sketch.POINTS);
    sketch.vertex(
      -my_object.R[0][0] / 1000,
      -my_object.R[2][0] / 1000,
      my_object.R[1][0] / 1000
    );
    sketch.endShape();
    sketch.pop();

    sketch.push();
    sketch.strokeWeight(3);
    sketch.stroke(255, 0, 0); //RED
    sketch.line(0, 0, 0, 10000, 0, 0);
    sketch.stroke(0, 255, 0); //GREEN
    sketch.line(0, 0, 0, 0, 10000, 0);
    sketch.stroke(0, 0, 255); //BLUE
    sketch.line(0, 0, 0, 0, 0, 10000);
    sketch.pop();

    document.getElementById("param").innerHTML =
      "Period: " +
      sketch.round(my_object.PERIOD, 2) +
      " min <br />Latitude: " +
      sketch.round(my_object.lat[0], 2) +
      "° <br />Longitude: " +
      sketch.round(my_object.lon[0], 2) +
      " ° <br />Epoch: " +
      my_object.EPOCH +
      "<br />GMST: " +
      sketch.round(my_object.GMST) +
      " °<br />Inclination: " +
      sketch.round((my_object.INCLINATION * 180) / Math.PI, 2) +
      " °";

    let canvas = document.getElementById("myCanvas");
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
  };
};

new p5(s3);
