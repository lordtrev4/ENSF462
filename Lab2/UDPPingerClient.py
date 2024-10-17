import time
from socket import *

# Create a UDP socket

serverAddress = ('localhost', 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)

# make a list for RTT values

rttList = []
successfulPings = 0

print("Pinging the server...")
for number in range(1,11):
    # creating the message
    message = f"Ping {number} {time.time()}"

    # Record send time
    sendTime = time.time()
    
    # sending the message
    clientSocket.sendto(message.encode(), serverAddress)

    try:
        #Wait for response
        response, server = clientSocket.recvfrom(1024)

        #Calculate RTT
        rtt = time.time() - sendTime
        rttList.append(rtt)
        successfulPings += 1

        #Print response
        print(f"Reply from {server[0]}: {response.decode()} in {rtt:.4f} seconds")
    
    except timeout:
        print(f"Request timed out.")

    # wait for 1 second before pinging agian
    time.sleep(1)

# Print the statistics
if successfulPings > 0:
    minRTT = min(rttList)
    maxRTT = max(rttList)
    avgRTT = sum(rttList) / successfulPings
    packetLossRate = (10 - successfulPings) / 10 * 100

    print(f"\n--- Ping statistics for {serverAddress[0]} ---")
    print(f"10 packets transmitted, {successfulPings} received, {packetLossRate}% packet loss")
    print(f"Round Trip Times: Min = {minRTT:.4f}s, Max = {maxRTT:.4f}s, Avg = {avgRTT:.4f}s")

else:
    print("All requests timed out.")

clientSocket.close()