import socket

print("\tFIEK-TCP Klienti")
print("\tLenda : Rrjeta Kompjuterike")
print("\tAsistenti : Edon Mustafa")
print("\tGrupi 10")
print("\tUrtina Deskaj")
print("\tOlta Abazi")
print("\tShkelqim Rexhepi")
print("\tArberie Burrniku\n\n\n")

host = socket.gethostname()
serverAddress="localhost"
port = 8085

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.connect((serverAddress,port))
message = input('Fjalia me shkronja te vogla: ')
serverSocket.send(message.encode("ascii"))
teDhenat = serverSocket.recv(1024)
print("Rezultati nga serveri: "+ teDhenat.decode("ascii"))
serverSocket.close();