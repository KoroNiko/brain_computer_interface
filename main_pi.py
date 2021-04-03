import socket
import serial
import sys

from pi_client import *

def main():
	channel = serial.Serial('/dev/ttyACM0', 9600)

	pi_client = piConnectionClient()


	while True:
		data = pi_client.receiveData()

		if 'q' in data.decode('utf-8') or 'Q' in data.decode('utf-8'):
			pi.closeConnection()
			sys.exit()

		if data.decode('utf-8') == 'FRONT':
			channel.write(b'1')
		elif data.decode('utf-8') == 'BACK':
			channel.write(b'2')
		elif data.decode('utf-8') == 'LEFT':
			channel.write(b'3')
		elif data.decode('utf-8') == 'RIGHT':
			channel.write(b'4')



if __name__ == '__main__':
	main()