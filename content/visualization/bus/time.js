/**
 * Generate the stable initial conditions for n buses
 * on a loop, which is just equally spaced.
 */
function initialConditions(n) {
  let arr = new Array(n);
  for (let i = 0; i < n; i++) {
    arr[i] = i * 360/n;
  }
  return arr;
}


/**
 * Given positions, v0, and gamma,
 * return the angular velocity of
 * buses.
 */
function thetaVelocity( thetas, v0, gamma ) {
  const velocities = thetas.slice();
  for (let i = 0; i<thetas.length; i++) {
    let dist = i === thetas.length-1 ?
               thetas[0]-thetas[i] :
               thetas[i+1] - thetas[i];
    dist = (dist < 0 ? dist + 2*Math.PI : dist) % 2*Math.PI;
    velocities[i] = v0 * (1 - gamma * dist);
  }
  return velocities;
}

/**
 * Given a vector, the time, a function that evaluates the
 * time derivative of the vector, and a timestep,
 * integrate that vector to the next step (using RK4).
 */
function integrate(y, t, dydt, dt) {
  const k1 = dydt(t, y);

  const y2 = y.slice();
  for (let i = 0; i<y.length; i++) {
   y2[i] = y[i] + dt/2 * k1[i];
  } 
  const k2 = dydt(t + dt/2, y2);

  const y3 = y.slice();
  for (let i = 0; i<y.length; i++) {
   y3[i] = y[i] + dt/2 * k2[i];
  } 
  const k3 = dydt(t + dt/2, y3);

  const y4 = y.slice();
  for (let i = 0; i<y.length; i++) {
   y4[i] = y[i] + dt * k3[i];
  } 
  const k4 = dydt(t + dt, y4);

  const solution = y.slice();
  for (let i = 0; i<y.length; i++) {
    solution[i] = y[i] + dt/6 * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]);
  }
  return solution;
}
