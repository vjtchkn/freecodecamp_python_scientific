# Extend socket program to prompt the user for the URL
# Use split() to break URL into parts
# Use try / except to handle bad URLs

import socket

url = input("Enter URL: ")
url_split = url.split("/")
try:
    host = url_split[2]
except:
    print("Invalid URL")
    exit()

# Create a socket and connect it to server on port 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host, 80))
except:
    print("Cannot connect to host")
    exit()

# Command to send to the server
try:
    cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
except:
    print("Invalid URL")
    exit()

# Send the command
mysock.send(cmd)

# Receiving data back from the server 512 characters at a time
# Break if no data received
# Decode and print the data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

# Close the connection
mysock.close()
