let slider = document.getElementById("rayleigh-slider");
let label = document.getElementById("rayleigh-label")

let emscript = document.getElementById('emscript');

let handleInput = (evt) => {
  const exponent = parseInt(slider.value);
  if (Module && Module.set_rayleigh) {
    Module.set_rayleigh(Math.pow(10, exponent));
  }
  let displayRa;

  if (exponent <= 3) {
    displayRa = Math.pow(10, exponent)
  } else {
    displayRa = "10<sup>"+exponent+"</sup>";
  }
  label.innerHTML = `Ra = ${displayRa}`
};

slider.addEventListener('input', handleInput);
slider.addEventListener('mouseup', evt => evt.stopPropagation());
slider.value = 4;
emscript.onload = () => {
  Module.onRuntimeInitialized = () => {
    Module.set_rayleigh(Math.pow(10, slider.value));
    console.log('loaded');
    handleInput();
  };
};
