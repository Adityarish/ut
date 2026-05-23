import socket
import json
import threading

HOST = '127.0.0.1'
PORT = 5001

clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append(conn)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = json.loads(data.decode())
            print(f"[{addr}] {message['name']} : {message['msg']}")

            broadcast(message,conn)
    except:
        print(f"[Disconnected] {addr}")
    finally:
        clients.remove(conn)
        conn.close()

def broadcast(message, sender_conn):
    for client in clients:
        if client != sender_conn:
            try:
                client.send(json.dumps(message).encode()) # client send krega fir json.dump(message).encode()
            except:
                pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()
    print(f"[SERVER STARTED] listening on {HOST} : {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()