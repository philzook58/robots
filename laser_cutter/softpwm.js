
var pin = "USR2";
var val = 1.0;

var freq = 60;
var period = 1/freq*1000;



function setPwm(){
  b.digitalWrite(pin,b.HIGH);
  setTimeout(period * val, unsetPwm);
}

function unsetPwm(){
  b.digitalWrite(pin,b.LOW);
  setTimeout(period * (1.0-val), setPwm);
}
