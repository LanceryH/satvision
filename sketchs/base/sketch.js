function preload() {
  param_js = loadJSON("../../jsons/param.json");
}

function setup() {
  cnv = createCanvas(windowWidth, windowHeight, WEBGL);
  cnv.position(0, 0, "fixed");
  angleMode(DEGREES);
}

function draw() {
  background(0);
  clear();
  orbitControl(1, 1, 1);
  localStorage.setItem("data_local", JSON.stringify(param_js["val"]));
}
