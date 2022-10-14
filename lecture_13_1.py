# HTTP Request in Python
import socket

# Create a socket and connect it to server on port 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))

# Command to send to the server
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()

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
