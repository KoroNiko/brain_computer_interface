# import python modules
import sys

# import external libraries
import numpy as np
np.set_printoptions(suppress=True)

# import custom libraries
from filters import *
from fft_features import *
from data_receive import *
from models import *
# from pi_bridge import *


def main():
	filters = Filter()
	transform = Transform()
	model = KerasModels()
	# pi = piConnectionServer()

	while True:
		x = input("Enter 1 to start recording and press 'q' or 'Q' to exit: ")
		if x == '1':
			data_getter = GanglionDataReceiver()

			eeg_recording = data_getter.get_signal()
			o1 = eeg_recording[0]
			o2 = eeg_recording[1]

			# NOTCH WAS CALCULATED BUT WAS PASSED IMMEDIATELY TO BANDPASS SO IT WASNT VISIBLE. PLOTS ERROR
			o1_notch = filters.notch_filter(o1)
			o2_notch = filters.notch_filter(o2)

			o1_filtered = filters.bp_filter(o1_notch)
			o2_filtered = filters.bp_filter(o2_notch)


			# SAVING ARRAYS FOR PLOTTING
			# np.savez('alpha_front', o1=o1, o2=o2, o1_notch=o1_notch, o2_notch=o2_notch, o1_filtered=o1_filtered, o2_filtered=o2_filtered)
			# np.savez('alpha_back', o1=o1, o2=o2, o1_notch=o1_notch, o2_notch=o2_notch, o1_filtered=o1_filtered, o2_filtered=o2_filtered)			
			# np.savez('alpha_left', o1=o1, o2=o2, o1_notch=o1_notch, o2_notch=o2_notch, o1_filtered=o1_filtered, o2_filtered=o2_filtered)
			# np.savez('alpha_right', o1=o1, o2=o2, o1_notch=o1_notch, o2_notch=o2_notch, o1_filtered=o1_filtered, o2_filtered=o2_filtered)

			# Inputs are returned normalized in the range of [0, 1]. Check fft.py normalize()
			o1_sum = transform.sum_fourier_trans(o1_filtered)
			o2_sum = transform.sum_fourier_trans(o2_filtered)

			# append lists and then convert them to np array
			nn_input = np.asarray(o1_sum + o2_sum)
			nn_input.shape = (1, 8)

			predictions = model.nn_model(nn_input)
			predictions_list = [x.item() for x in predictions]
			predicted_movement = predictions_list.index(max(predictions_list))
			if predicted_movement == 0:
				print(predicted_movement, '   BACK')
				# pi.sendData('BACK')
			elif predicted_movement == 1:
				print(predicted_movement, '   FRONT')
				# pi.sendData('FRONT')
			elif predicted_movement == 2:
				print(predicted_movement, '   LEFT')
				# pi.sendData('LEFT')
			else:
				print(predicted_movement, '   RIGHT')
				# pi.sendData('RIGHT')

		elif x == 'q' or x == 'Q':
			# pi.sendData('q Q Entered. Exiting...')
			# pi.closeConnection()
			sys.exit()


if __name__ == '__main__':
	main()