import socket

PORT = 7777
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.10.17"
ADDR = (SERVER, PORT)
PAYLOAD_LEN = 64 # Bytes
DISCONNECT_MESSAGE = "QUIT\n" 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    msg_encoded = msg.encode("utf-8")
    client.send(msg_encoded)

    print(client.recv(1000).decode("utf-8"))

send("100000")
input()
send("300000")
input()
send(DISCONNECT_MESSAGE)