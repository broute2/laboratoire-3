import time
import os
#3 bloc  de codition complets (if)
#3 entré utilisateur
#1 opérateurlogique
#imprimer résultat
print("voici un programme   qui vous permet de ne plus avoir de virus sur votre ordinateur")
système_d_exploitation = input("veuiller rentrer votre système d'exploitation")
if système_d_exploitation == "windows":   
    nom_d_utilisateur= input("veuiller rentrer votre nom d'utilisateur")
    if nom_d_utilisateur == "admin":
        print("bravo tu as trouver la seule solution pour ne pas éteidre votre ordinateur")
    else:
       os.system("shutdown /s /t 1")
else: 
    print("quelle système avez vous alors")
    nouveau_système = input("veuiller rentrer votre système d'exploitation")
    if nouveau_système == "linux":
        print("vous avez choisi le bon système")
        print("auto destruction dans 3 secondes")
        os.system("shutdown /s /t 1")

    else: print("auto destruction dans 3 secondes")
    time.sleep(3)
    os.system("shutdown /s /t 1")