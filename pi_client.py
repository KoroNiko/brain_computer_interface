import socket
import sys

class piConnectionClient:
	def __init__(self):
		self.sock = socket.socket()
		self.port = 5100
		# Enter PC IP address
		self.host = '192.168.1.6'
		self.sock.connect((self.host, self.port))
		print('Trying to connect to: ', self.host)

	def receiveData(self):
		try:
			msg = self.sock.recv(self.port)
		except socket.error:
			sock.close()
			print('A socket error occurred. Exiting...')
			sys.exit(2)

		return msg

	def closeConnection(self):
		self.sock.close()


if __name__ == '__main__':
	pi = piConnectionClient()

	while True:
		data = pi.receiveData()

		if 'q' in data.decode('utf-8') or 'Q' in data.decode('utf-8'):
			pi.closeConnection()
			sys.exit()

		print('I just read:  ', data)
