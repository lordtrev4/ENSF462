import socket

def client_start():
    user1name = input("Enter your name: ") # name inputting

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket
    serveraddress = ('192.168.0.92', 6000)
    
    clientsocket.connect(serveraddress) # connecting to the server
    print(f"Connecting to {serveraddress[0]}:{serveraddress[1]}") # check if the client is connected to the right IP address and port

    try:
        print(f"Sending name {user1name} to server.")
        clientsocket.send(user1name.encode()) # sending the name of the client to server

        user2name = clientsocket.recv(1024).decode() # receiving the name from the server
        print(f"Connected with {user2name}")

        # chat starts now that connection is established
        while True:
            clientmessage = input(f"{user1name}: ") # client message 
            clientsocket.send(clientmessage.encode())

            if clientmessage.lower() == 'bye': #ends if client sends bye
                print("You have ended the conversation.")
                break

            servermessage = clientsocket.recv(1024).decode() 
            print(f"{user2name}: {servermessage}")

            if servermessage.lower() == 'bye': #ends if server sends bye
                print("Server has ended the conversation.")
                break
    finally:
        clientsocket.close() # closing the connection
        print("Connection closed.")

if __name__ == "__main__":
    client_start()