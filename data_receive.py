import numpy as np
import nnpy
import json
import os

class GanglionDataReceiver:
    def __init__(self):
        self.ENDPOINT = 'tcp://0.0.0.0:8080'
        self.cs = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
        self.cs.connect(self.ENDPOINT)
        self.cs.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')

        self.duration = 0.3
        self.freq = 440

    def get_signal(self):
        alpha_arr = np.zeros((2,1604))
        for i in range(alpha_arr.shape[1]):
            json_data = self.cs.recv()
            data_ls = json.loads(json_data)
            alpha_arr[0][i] = data_ls[0]
            alpha_arr[1][i] = data_ls[1]
            timestamp = data_ls[2]
            
            if i in {0, 401, 802, 1203, 1603}:
                os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (self.duration, self.freq))
        # print(timestamp)

        self.cs.close()
        return alpha_arr

# if __name__ == '__main__':
    # main = GanglionDataReceiver()
    # main.get_signal()