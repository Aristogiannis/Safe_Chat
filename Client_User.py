from decimal import Decimal
import socket
import sys
import random
import math
import time

p = random.randint(5, 15)
q = random.randint(5, 15)
k = random.randint(1,5)
i = 1
j = 1

while i < (p // 2):
    i += 1
    if p % i == 0:
        p = random.randint(5, 15)
        i = 1

while j < (q // 2):
    j += 1
    if q % j == 0:
        q = random.randint(5, 15)
        j = 1

n = p * q
phi = (p - 1) * (q - 1)

while True:
    e = random.randint(1, phi)
    if e % phi == 1:
        break

d = (k*phi +1) / e

def RSA_enc(msg,n,e):

    num_list = []
    res = ""

    for letter in msg:
        num_list.append(ord(letter))

    for num in range(len(num_list)):
        res += str(num_list[num])

    encrypted = int(pow(int(res), e))
    encrypted1 = int(math.fmod(encrypted, n))

    return str(encrypted1)

def RSA_dec(msg,d,n):
    print(msg)
    msg1 = (float(msg)** d ) % n
    print(msg1)
    ms1 = msg1 * 100
    print(ms1)
    f = chr((int(ms1)))
    return f

try:
    socket_server = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    sport = 8080
except:
    print("local error")

print('This is your IP address: ', ip)
server_host = input('Enter friend\'s IP address:')
name = input('Enter your name: ')

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
print(server_name, ' has joined...')
socket_server.send(str(str(n) + "/" + str(e)).encode())
public = socket_server.recv(1024).decode()
public = public.split("/")


print(public[1], public[0])

while True:
    #message reciever
    message = (socket_server.recv(1024)).decode()
    message = RSA_dec(message,d,n)
    print(server_name, ":", message)

    #message send
    message = input("me : ")
    if message == "quit()": #stop messaging
        message = "User has been disconected"
        message = RSA_enc(message, int(public[0]), int(public[1]))
        socket_server.send(message.encode())
        break
    else:
        message = RSA_enc(message,int(public[0]), int(public[1])) #RSA encode
        socket_server.send(message.encode())


