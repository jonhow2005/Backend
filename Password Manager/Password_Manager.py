masterpwd = str("test")
import Encrypter
import Decrypter

if str(input("Master Password: ")) != masterpwd:
    x = 0;
    while x > -1:
        print(quit);
        input();
        x = x+1


def View():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            if line == " ":
                break 
            elif line == "":
                break

            templine = line.split("|");   
            print("")
            Decrypter.decrypt(templine[0])
            print("Application: " + Decrypter.output);
            Decrypter.decrypt(templine[1])
            print("Username: " + Decrypter.output);
            Decrypter.decrypt(templine[2])
            print("Password: " + Decrypter.output
);
            

def Add():
    application = str(input("Application: "))
    name = str(input("Name: "))
    pwd = str(input("Password: "))
    Encrypter.encrypt(application)
    application = Encrypter.output
    Encrypter.encrypt(name)
    name = Encrypter.output
    Encrypter.encrypt(pwd)
    pwd = Encrypter.output

    with open('passwords.txt','a') as f:
        f.write(application + "|" + name + "|" + pwd + "\n" + "");

def Rinse():
    open('passwords.txt', 'w').close()

while True:
    mode = str(input("What would you like to do? (View/Add/Rinse/End) :"))
    if mode == "View":
        View();
    elif mode == "Add" :
        Add();
    elif mode == "Rinse":
        Rinse();
    elif mode == "End":
        break;
    else:
        print("invalid");
        break;

