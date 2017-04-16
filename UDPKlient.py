from socket import *

server = "adresa"
port = 12000

clientSocket = socket(family=AF_INET, type=SOCK_DGRAM)

message = input("fjali me te vogla:")

clientSocket.sendto(message.encode("ASCII"),(server,port))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print(modifiedMessage.decode("ASCII"))