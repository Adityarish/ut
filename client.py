import socket 
import threading
import json

HOST = '127.0.0.1'
PORT = 5001

name = input("Enter your name")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

def receive():
    while True:
        try:
            data = client.recv(1024)
            if data:
                message = json.loads(data.decode())
                print(f"\n {message['name']}:{message['msg']}")

        except:
            print("Connection closed")
            break

def send():
    while True:
        msg = input()
        message = {
            "name" : name,
            "msg" : msg
        }

        client.send(json.dumps(message).encode())


receive_thread = threading.Thread(target=receive)
send_thread = threading.Thread(target=send)

receive_thread.start()
send_thread.start()
                  
                