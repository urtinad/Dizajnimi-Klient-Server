from socket import *
import sys
import random
import socket
import time
import threading
import string
import math 
import datetime
import time
import thread

port = 8085
hosti = socket.gethostname()
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(10)
print("Serveri i gatshem per pranimin e te dhenave")

message, address = serverSocket.accept()
print('Nje connection u pranua nga: ', address)

data = message.recv(1024)
data = data.decode("utf-8")
dataUpper = data.upper()

def reverse(teksti):
    if len(teksti)<=1:
        return teksti
    return reverse(teksti[1:])+teksti[0]

def zanoret(teksti):
    zanore=['a','e','i','o','u','y','A','E','I','O','U','Y']
    nrzanore=0
    pergjigjja=""
    for i in range(0,len(teksti)):
        if (teksti[i] in zanore):
            nrzanore=nrzanore+1
    return nrzanore
    pergjigjja+="Teksti i derguar permban " + str(nrzanore)
    return pergjigjja

def faktoriel(n):
    if n == 0:
        return 1
    else:
        rezultat=n * faktoriel(n-1)
        return rezultat

def syprinaRrethir(n):
    s=n*n*3.14
    return s

def krahas(n,m):
    if (n>m):
        return "Numri "+str(n)+" eshte me i madh se "+str(m)
    elif m>n:
        return "Numri "+str(m)+" eshte me i madh se "+str(n)
    else:
        return "Numrat jane te barabarte"

def konverto(lista):
    
    if (len(lista) == 3):
        try:
            if lista[1] == "FTC":  # Fahrenheit to Kelvin
                rezultati = ((int(lista[2]) - 32) * (5.0 / 9))
                return rezultati

            elif lista[1] == "CTF":
                rezultati = (int(lista[2]) * (9 / 5) + 32)
                return rezultati

            elif lista[1] == "CTK":  # celsiustokelvin
                rezultati = (int(lista[2]) + 273.15)
                return rezultati

            elif lista[1] == "KTF":  # kelvintofahrenheit
                rezultati = (int(lista[2]) * (9 / 5) - 459.67)
                return rezultati

            elif lista[1] == "KTC":  # kelvintocelsius
                rezultati = (int(lista[2]) - 273.15)
                return rezultati

            elif lista[1] == "FTK":  # fahrenheittokelvin
                rezultati = ((int(lista[2]) + 459.67) * 5 / 9)
                return rezultati

            elif lista[1] == "PTK":  # poundtokilogram
                rezultati = (int(lista[2]) / 2.2046)
                return rezultati

            elif lista[1] == "KTP":  # kilogramtopound
                rezultati = (int(lista[2]) * 2.2046)
                return rezultati
            else:
                return "Ju lutem shkruani njeren nga metodat e perkrahura!"
        except:
            return "Ju lutem shkruani parametrat ne formatin e duhur!"
    else:
        return "Ju lutem shkruani numrin e duhur te parametrave!"


def kalkulatori(lista):
    
    if (len(lista) == 4):
        try:
            if lista[1] == "SHUMEZIMI":  
                rezultati = ((int(lista[2]) * int(lista[3])))
                return rezultati

            elif lista[1] == "HERESI":
                rezultati = float(int(lista[2]) / int(lista[3]))
                return rezultati

            elif lista[1] == "MBLEDHJA": 
                rezultati = (int(lista[2]) + int(lista[3]))
                return rezultati

            elif lista[1] == "ZBRITJA":  
                rezultati = (int(lista[2]) - int(lista[3]))
                return rezultati

            else:
                return "Ju lutem shkruani njeren nga metodat e perkrahura!"
        except:
            return "Ju lutem shkruani parametrat ne formatin e duhur!"
    else:
        return "Ju lutem shkruani numrin e duhur te parametrave!"

def StringLength(n):
    numrigjatesis=len(n)
    return "Fjala eshte e gjate "+str(numrigjatesis)+" karaktere"

edhena=dataUpper.split(' ')

if dataUpper == "PORT" : message.send(str("Porti juaj eshte: "+str(message.getpeername()[1])).encode("utf-8"))##getpeername e merr ip edhe portin si array per [0]==ip per [1]==port

elif dataUpper == "IP" : message.send(str("IP juaj eshte: "+str(message.getpeername()[0])).encode("utf-8"))

elif dataUpper == "HOST" : message.send(str("Emri i Klientit eshte: ").encode("utf-8")+socket.gethostbyname())

elif dataUpper =="TIME" :  message.send(str("Koha: "+str(datetime.datetime.now())).encode("utf-8"))

elif dataUpper =="KENO" : message.send(str(random.sample(range(1,80),20)).encode("utf-8"))

elif dataUpper == "PRINTO" :
    if(len(edhenat)>=2):
                    if edhenat[1]:
                        rezultati = ' '.join(edhenat)
                        message.send(str(rezultati).encode('utf-8'),addr)
                    else:
                         message.send("Ju lutem shkruani parametrin e dyte".encode("utf-8"))
    else: message.send("Ju lutem shkruani parametrin e dyte".encode("utf-8"))
#Metoda e bere nga Shkelqim Rexhepi
elif edhena[0] == "PRINTOREV" : message.send(str("Teksti juaj: " + str(reverse(edhena[1]))).encode("utf-8"))

elif edhena[0]=="ZANORE": message.send(str(zanoret(edhena[1])).encode("utf-8"))

elif edhena[0]=="FAKTORIELI": message.send(str(faktoriel(int(edhena[1]))).encode("utf-8"))

#Metoda e bere nga Olta Abazi
elif edhena[0]=="SYPRINARR": message.send(str(syprinaRrethir(int(edhena[1]))).encode("utf-8"))
#Metoda e bere nga Olta Abazi
elif edhena[0]=="KRAHASO": message.send(str(krahas(int(edhena[1]),int(edhena[2]))).encode("utf-8"))

#Metoda e bere nga Urtina Deskaj
elif edhena[0]=="GJATESIA": message.send(str(StringLength(edhena[1])).encode("utf-8"))

elif edhena[0] == "KONVERTO":
   rezultati = konverto(edhena) 
   message.send(str(rezultati).encode('utf-8'))

   #Metoda e bere nga Urtina Deskaj
elif edhena[0] == "KALKULATORI":
   rezultati = kalkulatori(edhena) 
   message.send(str(rezultati).encode('utf-8'))



else: message.send(str("Ju lutem shkruani nje komande te vlefshme".encode('utf-8')))

message.close()