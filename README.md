# brain_computer_interface
Code for the implementation of a Brain-Computer Interface as mentioned in this paper: https://www.mdpi.com/2079-9292/8/12/1387
***
### Dependencies
1. Python 3
   * [NumPy][1]
   * [SciPy][2]
   * [Keras][3] (with [TensorFlow][4] backend)
   * [nnpy][5]

2. Node.JS
   * [nanomsg for node][6]
   * [OpenBCI Node.js Ganglion SDK][7]

[1]: https://numpy.org/
[2]: https://www.scipy.org/
[3]: https://keras.io/
[4]: https://www.tensorflow.org/
[5]: https://github.com/nanomsg/nnpy
[6]: https://www.npmjs.com/package/nanomsg
[7]: https://www.npmjs.com/package/@openbci/ganglion

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

The [OpenBCI Ganglion][8] was used to get the EEG signals. The signals are send to the computer via Bluetooth

[8]: https://shop.openbci.com/products/ganglion-board?variant=13461804483
***

#### Preprocessing
#### Feature Extraction
#### Classification
#### Translation
