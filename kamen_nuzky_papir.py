import random

moznosti = ["kámen", "Nůžky", "Papír"]
print ("Zvolte: Kámen , Nůžky , Papír")
hrac = input()
pocitac = random.choice(moznosti)

print ("Počítač:", pocitac)

if hrac == pocitac:
    print ("Remíza!")
elif (hrac == "Kámen" and pocitac == "Nůžky") or (hrac == "Nůžky" and pocitac == "Papír") or (hrac == "Papír" and pocitac == "Kámen"):
    print ("Vyhrál jsi!")
else:
    print ("Prohrál jsi!")

