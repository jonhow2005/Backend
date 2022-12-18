import Hash
import sqlite3
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))

server.listen()



def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    print(username)
    c.send("Password: ".encode())
    password = Hash.hashFunction(c.recv(1024))
    print(password)
    
    conn = sqlite3.connect("userdata.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM userdata WHERE username = ?  AND password = ?", (username, password))
    
    if cur.fetchall():
        c.send("Login succesful!".encode())
    else:
        c.send("Login failed".encode())
        
        
while True:
    client, addr = server.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()