print("input encrypted message")    
encryptedmessage = str(input())
keyarray = [0,0,0,0] 
decryptedmessage = str("")

with open('Key.txt') as f:
    lines = f.readlines()

lines = str(lines)
lines = lines.replace("'", "")
lines = lines.replace("[", "")
lines = lines.replace("]", "")
key = lines

def dekey(text,array):
    xvar = int(0)
    while xvar < 3:
        for char in text: 
            array[xvar] = char
            xvar = int(xvar) + 1
            if xvar == 4:
                break
    larray = text.split("|")
    for x in larray:
        if int(larray.index(x)) > 0:
            array.append(int(x))

def decryptreversal(message):
   global decryptedmessage
   versedmessage = str("")
   for char in message:
        versedmessage = str(char + versedmessage)
   decryptedmessage = versedmessage

def deceasarcypher(message):
    global decryptedmessage
    r = int(keyarray[0])
    ceasarmessage = str("")
    for char in message:
        letter = ord(char)-r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    decryptedmessage = ceasarmessage

def depolygraph(message):
    global decryptedmessage
    polymessage = str("")
    for char in message:
        letter = int(ord(char))
        letter = keyarray.index(letter)
        letter = chr(letter+32-4)
        polymessage = str(polymessage + letter)
    decryptedmessage = polymessage


dekey(key,keyarray)
depolygraph(encryptedmessage)
deceasarcypher(decryptedmessage)
decryptreversal(decryptedmessage)
print(decryptedmessage)