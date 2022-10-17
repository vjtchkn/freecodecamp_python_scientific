# Change the socket program
# Counts number of received characters, stops displaying text after showing 3000 characters
# Retrieve the entire document, count characters and display it at the end

import socket

url = input("Enter URL: ")
if len(url) == 0:
    url = "http://data.pr4e.org/romeo.txt"
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
# Decode data and save them
document = ""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    document += data.decode()

# Close the connection
mysock.close()

# Print first 3000 characters and total length
print(document[:3000])
print(f"Total characters: {len(document)}")
