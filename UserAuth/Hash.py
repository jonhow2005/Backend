import random
hashoutput = str("")

asciisum = int(0)
numbersum = int(0)
alphastring = str("")
hashsum = int(0)

def hashFunction(inputString):
    ceasarnum = random.randint(1,5)
    global asciisum
    global numbersum
    global alphastring
    global hashsum
    global hashoutput
    
    for char in str(inputString):
        asciisum = int(ord(char)) + int(asciisum)
    for char in str(inputString):
        if char.isnumeric():
            numbersum = int(ord(char)) + int(numbersum)
    for char in str(inputString):
        if char.isnumeric() == False:
            letter = int(int(ord(char)) + int(ceasarnum))
            alphastring = str(alphastring + chr(letter))

    hashstr = str(asciisum % 10)
    if alphastring == str(""):
        hashstr = hashstr + "0"
    else:
        hashstr = hashstr + "1"


    if int((asciisum * asciisum) % 51) + 65 < 91:
        hashstr = str(hashstr + str(chr(int((asciisum * asciisum) % 51) + 65))) 
    else:
        hashstr = str(hashstr + str(chr(int((asciisum * asciisum) % 51) + 65 + 6)))

    if alphastring == str(""): 
        y = random.randint(4,10)
        x = int(0)
    
        while x < y:
            randInt = int(random.randint(0,52))
            if int(randInt + 65) < 91:
                alphastring = str(alphastring + str(chr(randInt + 65))) 
            else:
                alphastring = str(alphastring + str(chr(randInt + 65 + 6)))
            x = x + 1

    if int(numbersum % 20) < int(10):
        hashstr = str(hashstr + "0" + str(int(numbersum % 20)))
    else:
        hashstr = str(hashstr + str(int(numbersum % 20)))


    y = int(0)
    x = int(0)
    for char in str(int(asciisum * asciisum)):
        x = x + int(1)
        if x == 1:
            hashstr = str(hashstr + char)
    y = x
    if y % 2 == 0:
        hashstr = str(hashstr + "_")
    else:
        hashstr = str(hashstr + "-")
    x = int(0)
    for char in str(int(asciisum * asciisum)):  
        x = x + int(1)  
        if x == y:
            hashstr = str(hashstr + char)
    x = int(0)
    for char in str(int(asciisum * asciisum)):
        x = x + int(1)
        if y % 2 == 0:    
            if x == (y/2):
                hashstr = str(hashstr + char)
            if x == ((y/2) + 1):
                hashstr = str(hashstr + char)
        else:
            if x == ((y/2) - 0.5):
                hashstr = str(hashstr + char)
            if x == ((y/2) + 1.5):
                hashstr = str(hashstr + char)



    x = int(0)
    for char in alphastring:
        x = x + int(1)
        if x == 1:
            hashstr = str(hashstr + char)
    y = x
    if y % 2 == 0:
        hashstr = str(hashstr + "-")
    else:
        hashstr = str(hashstr + "_")  
    x = int(0)
    for char in alphastring:  
        x = x + int(1)  
        if x == y:
            hashstr = str(hashstr + char)
    x = int(0)
    for char in alphastring:
        x = x + int(1)
        if y % 2 == 0:    
            if x == (y/2):
                hashstr = str(hashstr + char)
            if x == ((y/2) + 1):
                hashstr = str(hashstr + char)
        else:
            if x == ((y/2) - 0.5):
                hashstr = str(hashstr + char)
            if x == ((y/2) + 1.5):
                hashstr = str(hashstr + char)

    for char in hashstr:
        hashsum = hashsum + int(ord(char))

    if hashsum % 75 > 9:
        hashstr = str(hashstr + str(int((hashsum % 75))))
    else:
        hashstr = str(hashstr + "0" + str(int((hashsum % 75))))

    hashoutput = str(str(hashstr) + str(ceasarnum))
    return hashoutput