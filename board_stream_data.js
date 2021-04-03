var nano = require('nanomsg');

var addr = 'tcp://0.0.0.0:8080';
var pub = nano.socket('pub');
pub.bind(addr);

pub.sndbuf(1);
console.log(pub.sndbuf());

const Ganglion = require('openbci-ganglion');
const k = require('openbci-utilities/dist/constants');
const verbose = true;
let ganglion = new Ganglion({
  debug:false, // Default: false
  verbose: verbose,
  sendCounts: false // Default: false
}, (error) => {
  if (error) 
  {
    console.log(error);
  } 
  else 
  {
    if (verbose) {
      console.log('Ganglion initialization completed');
    }
  }
});

function errorFunc (err) {
  throw err;
}

const accel = false;

ganglion.once(k.OBCIEmitterGanglionFound, (peripheral) => {
  ganglion.searchStop().catch(errorFunc);

  ganglion.on('sample', (sample) => {
    console.log(`Channel1: ${sample.channelData[0]*10**6},\nChannel2: ${sample.channelData[1]*10**6},
        \nTimeStamp: ${sample.timestamp}`);

    pub.send(JSON.stringify([sample.channelData[0]*10**6, sample.channelData[1]*10**6, sample.timestamp]));
  }); // End of sample event

  ganglion.on('accelerometer', (accelData) => {
    console.log('accelData', accelData);
  }); // End of accelerometer event

  ganglion.once('ready', () => {
    if (accel) 
    {
      ganglion.accelStart().then(() => {
        return ganglion.streamStart();
      }).catch(errorFunc);
    }
    else
    {
      ganglion.streamStart().catch(errorFunc);
    }
  }); // End of .once('ready')

  ganglion.connect(peripheral).catch(errorFunc);
});