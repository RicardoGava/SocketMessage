import socket
from subprocess import Popen, PIPE
from sys import exit as finish
from time import sleep

TCP_PORT = 24000
NETWORK_CLASS = 'C'
# Rede classe C possuí máscara de subrede 255.255.255.0, usada na maioria das redes domésticas.

myip = socket.gethostbyname(socket.gethostname())
network = str('.'.join(myip.split('.')[0:ord(NETWORK_CLASS) - 64]))
#print(f'Seu IP é {myip}')
#print(f'Sua rede é {network}{(68 - ord(NETWORK_CLASS))*".0"}')

# Executa o comando arp -a para obter todos endereços conectados à rede
process = Popen('arp -a', stdout=PIPE)
(output, err) = process.communicate()
process.wait()

output2str = str(output)

# Verifica se foi possível executar o comando
if output2str.find(network) == -1:
    print('Não foi possível executar o comando arp\nFinalizando em 6 segundos!')
    for i in range(1,7):
        print((7-i), end="\r")
        sleep(1)
    finish()

# Cria um array e preenche com todos ips da rede
ips = []

while output2str.find(network) != -1:
    ips.append(output2str[output2str.find(network):output2str.find(' ', output2str.find(network))])
    output2str = output2str[output2str.find(' ', output2str.find(network)):]

ips.remove(myip) # Remove o próprio ip
ips.remove(network + (67 - ord(NETWORK_CLASS))*'.0' + '.1') # Remove o ip do gateway

# Criação de socket TCP do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Procura pelo IP com a porta aberta
print(f'Procurando o ip com a porta {TCP_PORT} aberta, isso pode demorar um pouco dependendo de quantos dispositivos estão conectados em sua rede...')
serverip = ''
for ip in ips:
    if not client.connect_ex((ip, TCP_PORT)):
        serverip = ip
        print(f'{ip}: porta aberta')
        break
    else:
        print(f'{ip}: porta fechada')

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
        client.connect((serverip, TCP_PORT))

print('Conexão fechada!')
client.close()
sleep(2)
finish()
