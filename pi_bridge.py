import socket
import time
import sys

class piConnectionServer:
	def __init__(self):
		self.port = 5100
		self.sock = socket.socket()
		self.sock.bind(('', self.port))
		self.sock.listen(5)
		self.conn, self.addr = self.sock.accept()
		print('Got a connection from: ', self.addr)

	def sendData(self, data):
		data = bytearray(data, 'utf-8')
		self.conn.send(data)

	def closeConnection(self):
		self.conn.close()


# if __name__ == '__main__':
# 	pi = piConnectionServer()

# 	while True:
# 		x = input('Enter q or Q to quit: ')
# 		if x == 'q' or x == 'Q':
# 			pi.sendData('q Q Entered. Exiting...')
# 			pi.closeConnection()
# 			break

# 		pi.sendData('Hello from the Ubuntu Side')
