import numpy as np
from keras.models import load_model

class KerasModels:
	def __init__(self):
		self.model = load_model('trained_model.h5')

	def nn_model(self, input_data):
		return self.model.predict(input_data)