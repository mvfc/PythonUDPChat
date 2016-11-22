import socket
import time

HOST = '127.0.0.1'
PORT = 8888
PORT2 = 7997

def server():
	try:
		sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	except socket.error:
		sys.exit()
	sock1.bind((HOST, PORT))
	resposta = 'Mensagem recebida com sucesso.'

	while True:
		data, addr = sock1.recvfrom(1024)
		print('Mensagem recebida.')
		print(data)
		try:
			sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		except socket.error:
			sys.exit()
		time.sleep(2)
		sock2.sendto(resposta.encode('utf-8'), (HOST, PORT2))
		print('Resposta enviada')
		sock2.close()

server()