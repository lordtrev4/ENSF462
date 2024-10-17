#import socket module
from socket import *
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        if not message:
            return  # If message is empty, return

        filename = message.split()[1]
        f = open(filename[1:])  # Open the requested file
        outputdata = f.read()  # Read the file contents
        f.close()

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())  # Send HTTP response header
        connectionSocket.send("Content-Type: text/html\r\n".encode())  # Specify content type
        connectionSocket.send("\r\n".encode())  # End of headers

                #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())  # Send 404 response header
        connectionSocket.send("Content-Type: text/html\r\n".encode())  # Specify content type
        connectionSocket.send("\r\n".encode())  # End of headers
        connectionSocket.send("<h1>404 Not Found</h1>".encode())  # Send 404 error message
   
    except Exception as e:
        print(f"An error occurred: {e}")  # Log any other errors
        # Fill in start
        # Fill in end

        #Close client socket
    finally:
        connectionSocket.close()  # Close the client connection

        # Fill in start
        # Fill in end


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('localhost', 6789))  # Binding to localhost on port 8080
serverSocket.listen(1)  # Listen for incoming connections
#Fill in start
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() 
    #Fill in start #Fill in end
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    # start a new thread to handle the client
    thread = threading.Thread(target=handle_client, args=( connectionSocket,))
    thread.start()

serverSocket.close()

