from socket import *
import sys
import select

serverAddress="localhost"
port = 8085

try:
    address = (serverAddress, port)
    client_socket = socket(AF_INET, SOCK_DGRAM)
    numriKerkesave = 0
    while numriKerkesave<50:
        message = input('Fjalia me shkronja te vogla: ')
        if message.upper() == "EXIT": break
        client_socket.sendto(message.encode("utf-8"), address)

        recv_data, addr = client_socket.recvfrom(2048)

        print ("Pergjigja e serverit: ", recv_data.decode("utf-8"))
        numriKerkesave += 1

except:
    print("Ka ndodhur gabim gjate lidhjes!")
finally:
    client_socket.close()
