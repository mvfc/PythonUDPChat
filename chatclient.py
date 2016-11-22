import socket

HOST = '127.0.0.1'
PORT = 8888
PORT2 = 7997

def clientsend():
	try:
		sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error:
		sys.exit()
	msg = input('Digite a mensagem a ser enviada\n')
	sock1.sendto(msg.encode('utf-8'), (HOST, PORT))
	print('Mensagem enviada')

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
		resposta = clientreceive()
		print('Resposta recebida')
		print(resposta)

menu()