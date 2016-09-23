var b = require('bonescript');
var SERVO1 = 'P9_14';
var duty_min = 0.03;
var position = 0;
var increment = 0.1;

b.pinMode(SERVO, b.OUTPUT);
updateDuty();

function updateDuty(angle1,angle2) {
    // compute and adjust duty_cycle based on
    // desired position in range 0..1
    var position1 = Math.PI * angle1;
    var duty_cycle = (position1*0.115) + duty_min;
    b.analogWrite(SERVO1, duty_cycle, 60);
    console.log("Duty Cycle: " +
        parseFloat(duty_cycle*100).toFixed(1) + " %");
}


function changeAngle(x,y){

    angle1 = Math.PI * x/100
    updateDuty(angle1,angle2);


}



var prompt = require('prompt');
//
// Start the prompt
//
prompt.start();

//
// Get two properties from the user: username and email
//

function getXY(){
    prompt.get([{name:'X', pattern: /^[0-9]*$/}, {name:'Y', pattern: /^[0-9]*$/}], function (err, result) {
      //
      // Log the results.
      //
      console.log('Command-line input received:');
      console.log('  X: ' + result.X);
      console.log('  Y: ' + result.Y);
      changeAngle(result.X,result.Y);

      prompt.get({name:'Again',default:'y'},function(err,result){
        if(result.Again == 'y'){
          getXY();
        }
      });

    });
}

getXY();
