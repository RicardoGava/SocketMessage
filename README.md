## Comunicação local via socket
#### Esse é um teste de comunicação local via socket entre um ESP8266 e um programa em Python

&nbsp;
### Servidor:

Para instalar o arquivo na placa de desenvolvimento ESP8266 é necessário ter o [ESP8266_Arduino Core](https://github.com/esp8266/Arduino) em sua IDE.

Certifiquece ao instalar o código em sua placa de alterar o SSID e Password para os valores de sua rede.
```C++
#define SSID "*****"
#define PASSWD "*****"
```
Material para montagem do circuito:
- Placa de desenvolvimento NodeMCU ESP8266;
- Display 16x02 com adaptador de comunicação I2C;

Esquema de montagem:
![Montagem](montagem.jpg "Esquema de montagem")

---
### Client:

Existem dois programas Python nesse projeto. Um deles sabendo o IP o outro não sabendo o IP de seu servidor.

Para utilizar o com IP conhecido altere a constante antes de executar:
```Python
SERVER_IP = "192.168.1.20"
```
Para o IP que erá exibido no display do seu servidor.

O programa com IP desconhecido executara um comando arp -a em sua rede e verificar todos IPs conectados. Ao encontrar um deles com a porta 24000 aberta fechará conexão.

Setudo funcionar você poderá enviar mensagens do seu computador e o ESP8266.

O comando "led on" irá acentar um led na placa de desenvolvimento presente na porta 16. Para apagá-lo envie o comando "led off".

Divirta-se com o código, altere e me mostre o que fez de legal.