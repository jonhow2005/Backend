import random
polyrand = int(0)
errors = int(0)
keyarray = [0,0,0,0]
print("input message")
message = str(input())
encryptedmessage = str((""))

def reverse(message):
    global keyarray
    keyarray[1] = int(1)
    reversedmessage = str("")
    for char in message:
        reversedmessage = str((char + reversedmessage))
    global encryptedmessage
    encryptedmessage = reversedmessage

def cCypher(message):
    global keyarray
    keyarray[2] = int(1)
    r = int(random.randint(0,9))
    keyarray[0] = r
    ceasarmessage = str("")
    for char in message: 
        letter = ord(char)+r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    global encryptedmessage
    encryptedmessage = ceasarmessage
    
 
def polygraph(message):
    global errors
    errors = int(0)
    global keyarray
    keyarray[3] = int(1)
    rounds = int(126-32)
    polymessage = str("")
    polykey = (str(""))
    polyarray = []
    x = int(0)
    polyrand = int(random.randint(32,126))
    while x < rounds:
        while polyarray.count(polyrand) == 0:
            polyarray.append(polyrand)
            polykey = str(polykey + "|"+ str(polyrand))
            x = x+1    
        if polyarray.count(polyrand) != 0:
            if int(len(polyarray)) < int(99-32):
                polyrand = int(random.randint(32,99))
            else:
                polyrand = int(random.randint(32,126))
    for char in message:
        letter = polyarray[ord(char)-32]
        letter = chr(letter)
        if ord(letter) - 32 <= rounds: 
            polymessage = str(polymessage + letter)
        else:
            errors = errors + 1

    global encryptedmessage
    encryptedmessage = polymessage
    keyarray.append(str(polykey))



def chartest():
    rounds = int(input())
    x = int(0)
    while x < rounds:
        print(chr(x) + " " + str(x))
        x = x+1

def chartest(message):
    for char in message:
        print(int(ord(char)))

reverse(message)
cCypher(encryptedmessage)
polygraph(encryptedmessage)
key = ("")
for x in keyarray:
    key = str(str(key) + str(x))

with open("Key.txt", "w") as niggerscannot:
    niggerscannot.write(key) 

while errors > 0:
    print(str(errors) + " errors found")
    reverse(message)
    cCypher(encryptedmessage)
    polygraph(encryptedmessage)
        
    key = ("")
    for x in keyarray:
        key = str(str(key) + str(x))

    with open("Key.txt", "w") as niggerscannot:
        niggerscannot.write(key)  

print(encryptedmessage)