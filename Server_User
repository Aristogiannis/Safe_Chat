import socket
import random
import math
import time

p = random.randint(5, 15)
q = random.randint(5, 15)
k = random.randint(1, 5)

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
e = random.randint(1, phi)

while True:
    if e % phi > 0:
        break
    else:
        e += 1


d = (k * phi + 1) / e


print(e)
print(n)


def rsa_enc(msg, n, e):
    num_list = []
    res = ""

    for letter in msg:
        num_list.append(ord(letter))

    for num in range(len(num_list)):
        res += str(num_list[num])

    print(res)
    ires = int(res)
    encrypted = ires ** e
    print(encrypted)
    encrypted1 = encrypted % n
    print(encrypted1)
    return str(encrypted1 / 100)


def rsa_dec(msg, d, n):
    pass
    return msg


try:
    new_socket = socket.socket()
    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)
    port = 8080
except:
    print("local error")

new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your IP: ", s_ip)

name = input('Enter your name:')
new_socket.listen(1)

conn, add = new_socket.accept()
print("Received connection from ", add[0])

print('Connection Established. Connected From: ', add[0])
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
conn.send(name.encode())
conn.send(str(str(n) + "/" + str(e)).encode())
public = conn.recv(1024).decode()
public = public.split("/")

while True:
    message = input('me : ')  # message input

    if message == "quit()":  # stop messaging
        message = "User has been disconected"
        message = rsa_enc(message)
        conn.send(message.encode())  # RSA encoding function
        break
    else:
        # message send
        conn.send(rsa_enc(message, int(public[0]), int(public[1])).encode())  # RSA encoding function

        # message reciever
        message = conn.recv(1024).decode()
        message = rsa_dec(message, d, n)
        print(client, ':', message)
