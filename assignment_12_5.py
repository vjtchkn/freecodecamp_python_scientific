# Retrieve and print out header of specified url
import socket

url = input("Enter URL: ")
if len(url) == 0:
    url = "http://data.pr4e.org/intro-short.txt"

host = url.split("/")[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))

cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
