
lines = str("")
output = str("")
r = int(0)

def decrypt(message):
    global r
    global output
    global lines
    with open('Key.txt') as f:
        lines = f.readlines()
    lines = str(lines)
    lines = lines.replace("[","")
    lines = lines.replace("'","")
    lines = lines.replace("]","")
    r = int(lines)
    ceasarmessage = str("")
    for char in message:
        letter = ord(char)-r
        letter = chr(letter)
        ceasarmessage = str(ceasarmessage + letter)
    output = ceasarmessage
