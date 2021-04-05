# brain_computer_interface
Code for the implementation of a Brain-Computer Interface as mentioned in this paper: https://www.mdpi.com/2079-9292/8/12/1387
***
### Hardware
1. [Dagu Rover 5 Chassis][1]
2. [L298N Motor Driver Module][2]
3. [OpenBCI Ganglion][3]
4. [Raspberry Pi][4]
5. [Arduino UNO][5]

### Dependencies
1. [Python 3][6]
   * [NumPy][7]
   * [SciPy][8]
   * [Keras][9] (with [TensorFlow][10] backend)
   * [nnpy][11]

2. [Node.JS][12]
   * [nanomsg for node][13]
   * [OpenBCI Node.js Ganglion SDK][14]


## Overview
The aim of this project was to create a EEG-based Brain-Computer Interface (BCI) which:
- [x] is easy to use
- [x] is highly accurate
- [x] can control multiple systems with minor modifications

The project structure will be explained based on the block diagram of a typical BCI as shown below
<p align="center">
<img src="https://user-images.githubusercontent.com/24572643/113514022-02770980-9575-11eb-91ec-013245a26365.png" width="600" height="180">
</p>

-----------------------
#### Signal Acquisition
-----------------------
This BCI uses alpha brainwaves as the control signal. It is well known that when a someone closes their eyes, the amplitude of their alpha waves increases. Conversely, when someone opens their eyes, the amplitude of their alpha waves decreases. This event is known as **_event-related synchronization/desynchronization (ERD/ERS)_**.

By taking advantage of this phenomenon, users can form binary sequences by closing or opening their eyes. Specifically, _an increased amplitude_ corresponds to a **'1'** and _a decreased amplitude_ corresponds to a **'0'**. A 'bit' recording lasts for **2** seconds. This system uses **4-bit** sequences, so a sequence recording lasts for **8** seconds.

The electrodes are placed at the following positions, according to the 10-20 system: 
- **Ch1**: _'O1'_
- **Ch2**: _'O2'_
- **REF**: _'A1'_
- **DGROUND**: _'A2'_

The OpenBCI Ganglion was used to get the EEG signals. The signals are send to the computer via Bluetooth.


------------------
#### Preprocessing
------------------
The signals were filtered with a notch filter to remove mains frequency (50 Hz)and a bandpass filter to preserve only the alpha band (5-15 Hz).
Both filters were IIR filters.

-----------------------
#### Feature Extraction
-----------------------
It's easier to explain the feature extraction procedure with a figure, so:

<p align="center">
<img src="https://user-images.githubusercontent.com/24572643/113576866-ff3d5580-9628-11eb-8c84-a9ee25d9291a.png">
</p>

The signals above are acquired from the 2 different regions _O1_ and _O2_. By summing the spectrum magnitudes for each 2-second interval, we can get a rough estimate about the user 
closing or opening their eyes. This 8 numbers are the features that are fed in the classifier.

-------------------
#### Classification
-------------------

----------------
#### Translation
----------------
[1]: https://www.pololu.com/product/1551
[2]: https://grobotronics.com/dual-motor-driver-module-l298n.html?sl=en
[3]: https://shop.openbci.com/products/ganglion-board?variant=13461804483
[4]: https://www.raspberrypi.org/
[5]: https://store.arduino.cc/arduino-uno-rev3
[6]: https://www.python.org/download/releases/3.0/
[7]: https://numpy.org/
[8]: https://www.scipy.org/
[9]: https://keras.io/
[10]: https://www.tensorflow.org/
[11]: https://github.com/nanomsg/nnpy
[12]: https://nodejs.org/en/
[13]: https://www.npmjs.com/package/nanomsg
[14]: https://www.npmjs.com/package/@openbci/ganglion
