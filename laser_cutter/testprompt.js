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

      prompt.get({name:'Again',default:'y'},function(err,result){
        if(result.Again == 'y'){
          getXY();
        }
      });

    });
}

getXY();
