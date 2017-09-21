/**
 * Given a context, draw a circular road into it.
 * Optionally also give an angle to rotate the road.
 */
function drawRoad(ctx, angle) {
  const size = Math.min(ctx.canvas.width, ctx.canvas.height);
  const center = size/2;
  const R = size/2;
  const d2r = Math.PI/180;

  const roadWidth = size/7;
  const curbWidth = 2;
  const dividerWidth = 5;
  const rot = angle || 0;

  // Prepare the context
  ctx.save();
  ctx.translate(center, center);
  ctx.lineDashOffset = -(R-roadWidth/2)*rot*d2r;

  // Draw the road pavement
  ctx.lineWidth = roadWidth;
  ctx.strokeStyle = '#AAB7B8';
  ctx.beginPath();
  ctx.arc(0, 0, R-roadWidth/2, 0*d2r,
    2.*Math.PI, anticlockwise=true);
  ctx.stroke();

  // Draw the road curbs
  ctx.lineWidth = curbWidth;
  ctx.strokeStyle = 'black';
  ctx.beginPath();
  ctx.arc(0, 0, R-curbWidth, 0*d2r,
    2.*Math.PI, anticlockwise=true);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, R-roadWidth, 0*d2r,
    2.*Math.PI, anticlockwise=true);
  ctx.stroke();

  // Draw the divider line
  ctx.lineWidth = dividerWidth;
  ctx.strokeStyle = '#F1C40F';
  ctx.setLineDash([20,25]);
  ctx.beginPath();
  ctx.arc(0, 0, R-roadWidth/2, 0*d2r,
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
  const d2r = Math.PI/180;
  const busWidth = size/6;
  const rot = angle || 0;

  ctx.save();
  ctx.translate(center, center);
  ctx.rotate(-angle * d2r + Math.PI/2);

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
