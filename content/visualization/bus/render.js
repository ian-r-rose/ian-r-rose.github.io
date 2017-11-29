/**
 * Load in the bus image.
 */
const bus = new Image();
bus.src = 'bus.svg';

/**
 * Given a context, draw a circular road into it.
 * Optionally also give an angle to rotate the road.
 */
function drawRoad(ctx, angle) {
  const size = Math.min(ctx.canvas.width, ctx.canvas.height);
  const center = size/2;
  const R = size/2;

  const roadWidth = size/7;
  const curbWidth = 2;
  const dividerWidth = 5;
  const rot = angle || 0;

  // Prepare the context
  ctx.save();
  ctx.translate(center, center);
  ctx.lineDashOffset = -(R-roadWidth/2)*rot;

  // Draw the road pavement
  ctx.lineWidth = roadWidth;
  ctx.strokeStyle = '#AAB7B8';
  ctx.beginPath();
  ctx.arc(0, 0, R-roadWidth/2, 0,
    2.*Math.PI, anticlockwise=true);
  ctx.stroke();

  // Draw the road curbs
  ctx.lineWidth = curbWidth;
  ctx.strokeStyle = 'black';
  ctx.beginPath();
  ctx.arc(0, 0, R-curbWidth, 0,
    2.*Math.PI, anticlockwise=true);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, R-roadWidth, 0,
    2.*Math.PI, anticlockwise=true);
  ctx.stroke();

  // Draw the divider line
  ctx.lineWidth = dividerWidth;
  ctx.strokeStyle = '#F1C40F';
  ctx.setLineDash([30,35]);
  ctx.beginPath();
  ctx.arc(0, 0, R-roadWidth/2, 0,
    2.*Math.PI, anticlockwise=true);
  ctx.stroke();

  // Restore the rendering context.
  ctx.restore();
}

/**
 * Given a context, draw a bus on the
 * circular road. The optional angle
 * argument give the CCW angle from the x-axis
 * to draw the bus at (in degrees).
 */
let drawBus = function(ctx, angle) {
  const size = Math.min(ctx.canvas.width, ctx.canvas.height);
  const center = size/2;
  const R = size/2;
  const busWidth = size/6;
  const rot = angle || 0;

  ctx.save();
  ctx.translate(center, center);
  ctx.rotate(-angle + Math.PI/2);

  ctx.drawImage(bus, -busWidth/2, -center-10, busWidth, busWidth);

  ctx.restore();
}

/**
 * Given a context, a road angle, and a list of
 * bus angles, draw a bus scene.
 */
let drawScene = function(ctx, roadAngle, busAngles) {
  ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  drawRoad(ctx, roadAngle);
  for (let angle of busAngles) {
    drawBus(ctx, angle);
  }
}

/**
 * Given a canvas context, initial conditions and a a time
 * derivative function, animate the scene.
 */
function animate(ctx, Y, dYdT, dRdT) {
  let prevTime = undefined;
  let roadAngle = 0;
  const update = (time) => {
    // Compute the timestep, or have it be
    // zero if we are just starting
    dt = prevTime ? (time - prevTime)/1000. : 0.0;
    prevTime = time;
    // Integrate the positions in time
    let next = integrate(Y, 0, dYdT, dt);
    for (let i = 0; i < Y.length; ++i) {
      Y[i] = next[i]
    }
    // Possibly update the road position
    if (dRdT) {
      roadAngle += dt * dRdT;
    }
    drawScene(ctx, roadAngle, angles);
    requestAnimationFrame(update);
  };

  requestAnimationFrame(update);
}
