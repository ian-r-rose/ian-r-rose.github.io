function outputData () {
  var Ra = Module.rayleigh();
  var Nu = Module.nusselt();

  var element = document.getElementById('output');
  if (element) element.value = ''; // clear browser cache

  var outRa;
  var outNu = String(Math.round(Nu))
  if (Ra > 1000) {
    exponent = Math.log10(Ra);
    exponent = Math.floor(exponent);
    lower = Ra/Math.pow(10, exponent);
    lower = Math.floor(lower)
    if(lower == 1){
      outRa = "10<sup>"+exponent+"</sup>";
    }
    else {
      outRa = String(lower)+"x10<sup>"+exponent+"</sup>";
    }
  } else {
    outRa = String(Math.round(Ra));
  }
  if (element) {
    element.innerHTML = "Ra = " + outRa + "&nbsp; &nbsp; &nbsp;" + "Nu = " + outNu
  }
};
setInterval( outputData, 100);
