let socket;
let names = []; 
let sat_data;
let orbit_status = 0;
function preload() {
    img = loadImage(imagePath); // Use the image path passed from HTML
}

function setup() {
    cnv = createCanvas(windowWidth, windowHeight, WEBGL); // Create a drawing canvas
    cnv.position(0, 0, "fixed");
    angleMode(DEGREES);
    socket = io(); 

    socket.on('receive_data', function(data) {
        names = data["Names"];
        colors = data["Colors"];
        sat_data = data;
    });

    socket.on('view_status', function(data) {
        orbit_status = data["Orbit"];
    });
}

function draw() {
    console.log(orbit_status)
    resizeCanvas(windowWidth, windowHeight)

    clear();
    background(0);
    orbitControl(1, 1, 1);
    scale(0.02);
    perspective(180 / 3.0, width / height, 0.1, 15000000);

    push();
    texture(img);
    strokeWeight(0);
    rotateX(0);
    rotateY(-180);
    rotateZ(0);
    sphere(6371, 24, 24);
    pop();  

    if (names.length > 0) {    
        for (let i = 0; i < names.length; i++) {
            push();
            strokeWeight(10);
            stroke(colors[i]);
            beginShape(POINTS);
            vertex(sat_data[names[i]][0][0]/1000, sat_data[names[i]][1][0]/1000, sat_data[names[i]][2][0]/1000);
            endShape();
            pop();
        }
    }
    if (orbit_status == 1) {
        for (let i = 0; i < names.length; i++) {
            push();
            strokeWeight(1);
            stroke(colors[i]);
            beginShape();
                for (let j = 0; j < sat_data[names[0]][0].length; j++) {
                vertex(sat_data[names[i]][0][j]/1000, sat_data[names[i]][1][j]/1000, sat_data[names[i]][2][j]/1000);
                }
            
            noFill();
            endShape();
            pop();
        }
    }
}
