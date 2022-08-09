import socket
import threading

#Constants
SERVER = '0.0.0.0'#socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
BUFFER_SIZE = 1024


def handle_client(openSocket):
    while True:
        message, clientAddress = openSocket.recvfrom(BUFFER_SIZE)
        decodedMessage = message.decode(FORMAT)
        print(f"[{clientAddress}]:: Message received.")
        file = open("./records.txt", "a")
        file.write(f"\n{decodedMessage}\n")
        print(decodedMessage)
        file.close()
        

def start():
    print(f"Start/ing UDP Server...")
    serverAddresses = {}
    sockets = {}
    file = open("./records.txt", "a")
    
    #Create the sockets
    for socketNum, port in enumerate(range(2100,2101)):
        serverAddresses[socketNum] = (SERVER, port)
        sockets[socketNum] = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockets[socketNum].bind(serverAddresses[socketNum])
        file.write(f"\n[LISTENING]:: Server is listening on {serverAddresses[socketNum]}\n")
        print(f"\n[LISTENING]:: Server is listening on {serverAddresses[socketNum]}\n")
        file.write(f"{sockets[socketNum]}")
        print(sockets[socketNum])
        
    file.close()   

    #Begin each thread
    for openSocket in sockets:
        #We require a thread for each socket to listen
        thread = threading.Thread(target=handle_client, args=(sockets[openSocket]))
        thread.start()

if __name__ == '__main__':
    start()