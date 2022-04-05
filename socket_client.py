import socket
from subprocess import Popen, PIPE
from sys import exit as finish
from time import sleep

TCP_PORT = 24000
SERVER_IP = "192.168.1.20"

# Criação de socket TCP do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, TCP_PORT))

# Pede para entrar com uma mensagem para enviar
print('Digite sua mensagem para o servidor (para sair digite /quit): ')
msg = ''
while msg != '/quit':
    msg = input()
    if (msg != '/quit'):
        client.sendall((msg + chr(10)).encode('UTF-8')) # Adiciona um enter na mensagem e envia para o servidor
        sleep(0.2)
        client.close() # Fecha conexão com servidor
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, TCP_PORT))

print('Conexão fechada!')
client.close()
sleep(2)
finish()
