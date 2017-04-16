from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("Serveri eshte i gatshem per pranim te te dhenave")

while True:
    message, clientAddress = serverSocket.recvfrom(1024)
    print("Mesazhi i pranuar: " + message.decode("ASCII"))
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
