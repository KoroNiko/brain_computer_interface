from scipy.fftpack import fft

import numpy as np

class Transform:
	def __init__(self):
		# 2 second interval indices to split the signal
		self.split_intervals = [[0, 401], [401, 802], [802, 1203], [1203, 1604]]
		# Alpha important frequencies indices. 14: 7.48, 26: 13.47
		self.important_freqs = [14, 27]
		# Length of studied signal
		self.signal_length = 401

	def split_signal(self, signal):
		return np.reshape(signal, (4, 401))

	def fourier_trans(self, signal):
		signal_fft = fft(signal)
		transform = np.abs(signal_fft[0:self.signal_length//2])
		return transform

	def sum_fourier_trans(self, signal):
		reshaped_signal = self.split_signal(signal)
		alpha_sum_list = []
		for i in range(reshaped_signal.shape[0]):
			fft_signal = self.fourier_trans(reshaped_signal[i, :])

			alpha_sum = np.sum(fft_signal[self.important_freqs[0]:self.important_freqs[1]])
			alpha_sum_list.append(alpha_sum)

		return alpha_sum_list

	def normalize(self, ls):
		norm_ls = list()
		for x in ls:
			x_norm = (x - min(ls)) / (max(ls) - min(ls))
			norm_ls.append(x_norm)

		return norm_ls