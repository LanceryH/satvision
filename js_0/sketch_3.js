function setup() {
  let canvas = createCanvas(100, 100);
  canvas.position(0, 0);
  const myWorker = new Worker("../js_1/sketch_1.js");
}

function draw() {
  console.log("doing something");
}
