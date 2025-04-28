/* Generates the image at path game/images/break.png
 *
 * This is p5.js code,
 * see/run it online at https://editor.p5js.org/p5rry/sketches/SET27NDue */

function setup() {
    // Width and height of the image
    // The final image is actually twice as big as these values,
    // so take your desired width/height and divide them by two
    const w = 360;
    const h = 540;

    // Higher number means a "spikier" image
    const noiseScale = 0.05;

    // General setup
    createCanvas(w, h);
    noStroke();

    // Draw the pixels
    for (let y = 0; y < h; y++) {
        for (let x = noise(noiseScale * y) * w; x < w; x++) {
            fill(random(256), random(256), random(256));
            square(x, y, 2);
        }
    }
}

// Everything is drawn in the setup function, so draw should do nothing
function draw() {}
