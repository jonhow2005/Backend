import random
key = ""
output = str("")
r = int(random.randint(0,9))
key = int(r)

def encrypt(message):
    global key
    global r
    global output
    ceasarmessage = str("")
    for char in message: 
        letter = ord(char)+r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    output = ceasarmessage
    with open('Key.txt', 'w') as f:
        f.write(str(key))
