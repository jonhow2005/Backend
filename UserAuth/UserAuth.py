import sqlite3
import Hash
import os
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")
gibble = True
while gibble == True:
    print("Register/Deregister/Exit")
    response = str(input())
    if response == "Exit":
        gibble = False; 
    elif response == "Deregister":
        print("Account Username:")
        userVar = input()
        cur.execute("DELETE FROM userdata WHERE (username) VALUES (?)", (userVar))
    elif response == "Register":
        print("Username:")
        userVar = input()
        print("Password:")
        passVar = input()
        username, password = userVar, Hash.hashFunction(passVar.encode())
        cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username, password))
        conn.commit()