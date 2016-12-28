import socket

HOST = '127.0.0.1'
PORT = 8888
PORT2 = 7997

def clientsend():
	try:
		sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error:
		sys.exit()
	msg = input('Type the message to be sent\n')
	sock1.sendto(msg.encode('utf-8'), (HOST, PORT))
	print('Message sent')

def clientreceive():
	try:
		sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error:
		sys.exit()
	sock2.bind((HOST, PORT2))
	data, addr = sock2.recvfrom(1024)
	sock2.close()
	return data

def menu():
	while True:
		clientsend()
		answer = clientreceive()
		print('Answer received')
		print(answer)

menu()
