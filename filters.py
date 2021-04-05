from scipy import signal

import numpy as np

class Filter:
	def __init__(self):
		# Notch filter section
		self.w0 = 50 / (200 / 2)
		self.Q = 35
		self.b1, self.a1 = signal.iirnotch(self.w0, self.Q)

		# Bandpass filter section
		self.bp_order = 40
		# this is 20 but in the paper it says 15 so maybe it should change. This is the passband
		# https://www.mathworks.com/help/signal/ug/iir-filter-design.html
		# the above link is good to remember some stuff
		self.cutoff_freqs = [5/100, 15/100]
		# self.b2, self.a2 = signal.iirfilter(self.bp_order, [0.05, 0.2])
		self.b2, self.a2 = signal.iirdesign([0.05, 0.2], [0.04, 0.21], gpass=0.1, gstop=30)

	def notch_filter(self, x):
		# Return notch filtered signal
		return signal.filtfilt(self.b1, self.a1, x)

	def bp_filter(self, x):
		# Return bandpass filtered signal
		return signal.filtfilt(self.b2, self.a2, x)
