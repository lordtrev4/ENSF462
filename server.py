import socket

def server_start():
    user2name = input("Enter your name: ") # name inputting

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating a socket

    serveraddress = ('192.168.0.92', 6000)
    serversocket.bind(serveraddress)
    print(f"Server started on {serveraddress[0]}:{serveraddress[1]}") # check if the server is run on the right IP address and port

    serversocket.listen() # listening for connections

    (connect, address) = serversocket.accept() # creates a socket object connect to send and recieve data

    try:
        user1name = connect.recv(1024).decode() # receiving the name of the client
        print(f"Connected with {user1name}")

        print(f"Sending name {user2name} to client.")
        connect.send(user2name.encode()) # sending the name of the server to client

        # chat starts now that connection is established

        while True:
            clientmessage = connect.recv(1024).decode()
            print(f"{user1name}: {clientmessage}")

            if clientmessage.lower() == 'bye': #ends if client sends bye
                print("Client has ended the conversation.")
                break

            servermessage = input(f"{user2name}: ")
            connect.send(servermessage.encode()) # sending the message to the client

            if servermessage.lower() == 'bye': #ends if server sends bye
                print("You have ended the conversation.")
                break

    finally:
        serversocket.close()
        print("Connection closed.")

if __name__ == "__main__":
    server_start()