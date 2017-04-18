from socket import *
import random
from time import gmtime, strftime
import re
import sys
import select

def reverse(teksti):
    if len(teksti)<=1:
        return teksti
    return reverse(teksti[1:])+teksti[0]

def konverto(lista):
    if (len(lista) == 3):
        try:
            if lista[1] == "FTC":  # Fahrenheit to Kelvin
                rezultati = ((int(lista[2]) - 32) * (5.0 / 9))
                return rezultati

            elif teDhenat[1] == "CTF":
                rezultati = (int(lista[2]) * (9 / 5) + 32)
                return rezultati

            elif teDhenat[1] == "CTK":  # celsiustokelvin
                rezultati = (int(teDhenat[2]) + 273.15)
                return rezultati

            elif teDhenat[1] == "KTF":  # kelvintofahrenheit
                rezultati = (int(teDhenat[2]) * (9 / 5) - 459.67)
                return rezultati

            elif teDhenat[1] == "KTC":  # kelvintocelsius
                rezultati = (int(teDhenat[2]) - 273.15)
                return rezultati

            elif teDhenat[1] == "FTK":  # fahrenheittokelvin
                rezultati = ((int(teDhenat[2]) + 459.67) * 5 / 9)
                return rezultati

            elif teDhenat[1] == "PTK":  # poundtokilogram
                rezultati = (int(teDhenat[2]) / 2.2046)
                return rezultati

            elif teDhenat[1] == "KTP":  # kilogramtopound
                rezultati = (int(teDhenat[2]) * 2.2046)
                return rezultati
            else:
                return "Ju lutem shkruani njeren nga metodat e perkrahura!"
        except:
            return "Ju lutem shkruani parametrat ne formatin e duhur!"
    else:
        return "Ju lutem shkruani numrin e duhur te parametrave!"


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
def factorial(n):
    if n<0: return "Nuk mund te gjendet faktorieli per numra negativ!"

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

try:
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind(('localhost', 8085))
    while 1:
        print ("Serveri i gatshem per pranimin e te dhenave.. ")
        recv_data, addr = server_socket.recvfrom(2048)
        data = recv_data.decode("utf-8")
        dataUpper = data.upper();

        print("Klienti thirri metoden: ", dataUpper)
        teDhenat = dataUpper.split(' ')
        if teDhenat[0]:
            if teDhenat[0] == "PORT":
                addresaPlote = str(addr).replace(")", "")
                ndarja = str(addresaPlote).split(',')
                server_socket.sendto(str(ndarja[1]).encode("utf-8"), addr)

            elif teDhenat[0] == "IP":
                addresaPlote = str(addr).replace("(","")
                ndarja = str(addresaPlote).split(',')
                server_socket.sendto(str(ndarja[0]).encode("utf-8"), addr)

            elif teDhenat[0] == "KENO" :
                server_socket.sendto(str(random.sample(range(1,80),20)).encode("utf-8"), addr)

            elif teDhenat[0] == "FAKTORIEL":
                if(len(teDhenat)==2):
                    if teDhenat[1]:
                        rezultati = factorial(int(teDhenat[1]))
                        server_socket.sendto(str(rezultati).encode('utf-8'),addr)
                    else:
                        server_socket.sendto("Ju lutem shkruani parametrin e dyte".encode("utf-8"),addr)
                else: server_socket.sendto("Ju lutem shkruani parametrin e dyte ne rregull".encode("utf-8"),addr)
            elif teDhenat[0] == "PRINTO":
                if(len(teDhenat)>=2):
                    rezultati = ""
                    for i in range(1, len(teDhenat)):
                        rezultati += str(teDhenat[i]) + " "
                    server_socket.sendto(str(rezultati).encode('utf-8'),addr)
                else: server_socket.sendto("Ju lutem shkruani parametrin e dyte".encode("utf-8"),addr)

            elif teDhenat[0] == "TIME":
                rezultati = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                server_socket.sendto(str(rezultati).encode('utf-8'), addr)

            
            elif teDhenat[0] == "ZANORE": server_socket.sendto(str(zanoret(teDhenat[1])).encode("utf-8"),addr)

            elif teDhenat[0] == "KONVERTO":
                rezultati = konverto(teDhenat)
                server_socket.sendto(str(rezultati).encode('utf-8'), addr)

            else: server_socket.sendto("Ju lutem shkruani nje komande te vlefshme".encode('utf-8'),addr)
        elif teDhenat[0]=="SYPRINARR": server_socket.sendto(str(syprinaRrethir(int(teDhena[1]))).encode("utf-8"), addr)

        else: server_socket.sendto("Ju lutem shkruani nje komande".encode('utf-8'),addr)

except:
    print("Ka ndodhur gabim gjate lidhjes!", sys.exc_info()[0])
finally:
    server_socket.close()