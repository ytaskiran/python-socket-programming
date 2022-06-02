import socket 
import threading

PORT = 7777
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.10.17"
ADDR = (SERVER, PORT)
PAYLOAD_LEN = 64 # Bytes
DISCONNECT_MESSAGE = "QUIT\n" 


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def findAllNumbers(n):
    cb = int(pow(n, 1.0 / 3))
    num_list = []
    s = set()
    for i in range(1, cb - 1):
        for j in range(i + 1, cb + 1):
            sum = (i*i*i) + (j*j*j)
            if sum in s:
                num_list.append(sum)
            else:
                s.add(sum)
    
    return num_list

def handleClient(conn, addr):
    print(f"New connection, {addr} is connected")

    conn.send("\nHardy-Ramanujan numbers are the numbers that can be represented as the sum of two cubes for two different pairs.\n\nEnter a number to see Hardy-Ramanujan numbers up until to that number\n\n Type QUIT to disconnect\n\n".encode("utf-8"))

    while True:
        msg = conn.recv(PAYLOAD_LEN).decode("utf-8")
        print(f"{addr} sent the message {msg}, message length: {PAYLOAD_LEN}")
        print(msg)

        if msg == DISCONNECT_MESSAGE:
            print("Client requested to disconnect")
            break
        
        if (findAllNumbers(int(msg))):
            conn.send("\nHardy-Ramanujan numbers: ".encode("utf-8"))
            for each in findAllNumbers(int(msg)):
                conn.send((str(each)+" ").encode("utf-8"))
            conn.send("\n\n".encode("utf-8"))
            

    conn.send("Disconnecting from the server\n".encode("utf-8"))
    conn.close()

def start():
    server.listen()
    print(f"Server is listening - {SERVER}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleClient, args=(conn,addr))
        thread.start()
        print(f"Active Connections: {threading.activeCount() - 1}")
        

start()
