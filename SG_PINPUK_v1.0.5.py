#Database
pin = int(1234)
puk = int(4321)
trypin = int(4)
trypuk = int(4)
user_input = int(0000)
username = ()
Logged_in = False
i = 1
nachricht = int(0)

#Reset PIN
def new_pin():
    global pin
    pin = int(input("Wählen sie bitte einen neuen PIN aus: "))
    print("Ihre neue PIN lautet: " + str(pin))

#MotD
print("\n \n \n \n \n \n \n \n")
print("Wilkommen zu -ISP-")

#Main
while Logged_in == False:
    if i == 1:
        #Get - Name
        print("\nBenutzername: ")
        if username == username:
            username = input(str())
            print("\nGuten Tag " + username + " sie haben " + str(nachricht) + " Nachrichten")
        else:
            pass
        
        trypin -= 1
        trypuk -= 1

        #trypipn 3
        while trypin == 3:
            try:
                user_input = int(input("\nBitte geben sie ihre PIN ein: "))
            finally:
                if user_input != pin:
                    trypin -= 1
                    print("\nDie falsche PIN wurde eingegeben")
                    print("Sie haben noch " + str(trypin) + " PIN versuche übrig")
                else:
                    print("\nWilkommen " + username + ", sie haben sich erfolgreich eingelogged")
                    i -= 1
                    quit()
        #trypin 2   
        while trypin == 2:
            try:
                user_input = int(input("\nBitte geben sie ihre PIN ein: "))
            finally:
                if user_input != pin:
                    trypin -= 1
                    print("\nDie falsche PIN wurde eingegeben")
                    print("Sie haben noch " + str(trypin) + " PIN versuch übrig")
                else:
                    print("\nWilkommen " + username + ", sie haben sich erfolgreich eingelogged")
                    i -= 1
                    quit()
        #trypin 1
        while trypin == 1:
            try:
                user_input = int(input("\nBitte geben sie ihre PIN ein: "))
            finally:
                if user_input != pin:
                    trypin -= 1
                    print("\nDie falsche PIN wurde eingegeben")
                    print("Sie haben noch " + str(trypin) + " PIN versuche übrig")
                else:
                    print("\nWilkommen " + username + ", sie haben sich erfolgreich eingelogged")
                    i -= 1
                    quit()
        #trypin 0
        while trypin == 0:
            try:
                user_input = int(input("\nBitte geben sie ihre PUK ein: "))
            finally:
                if user_input != puk:
                    trypin -= 1
                    trypuk -= 1
                    print("\nDie falsche PUK wurde eingegeben")
                    print("Sie haben noch " + str(trypuk) + " PUK versuche übrig")
                else:
                    new_pin()
                    trypin = 4
                    trypuk = 4
        #trypuk 2
        while trypuk == 2:
            try:
                user_input = int(input("\nBitte geben sie ihre PUK ein: "))
            finally:
                if user_input != puk:
                    trypuk -= 1
                    print("\nDie falsche PUK wurde eingegeben")
                    print("Sie haben noch " + str(trypuk) + " PUK versuch übrig")
                else:
                    new_pin()
                    trypin = 4
                    trypuk = 4
        #trypuk 1
        while trypuk == 1:
            try:
                user_input = int(input("\nBitte geben sie ihre PUK ein: "))
            finally:
                if user_input != puk:
                    trypuk -= 1
                    print("\nDie falsche PUK wurde eingegeben")
                    print("Ihre PUK wurde zu oft falsch eingegeben")
                    print("Sim-Karte gesperrt")
                    quit()
                else:
                    new_pin()
                    trypin = 4
                    trypuk = 4
        #trypuk 0
        while trypuk == 0:
            try:
                print("Sim-Karte gesperrt")
                quit()
            finally:
                if user_input != puk:
                    trypuk -= 1
                    print("Sim-Karte gesperrt")
                    quit()
                else:
                    print("Sim-Karte gesperrt")
                    quit()
    else:
        Logged_in = True
quit()