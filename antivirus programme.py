while True:
    import time
    import os
#3 bloc  de codition complets (if)
#3 entré utilisateur
#1 opérateurlogique
#imprimer résultat
    print("voici un programme   qui vous permet de ne plus avoir de virus sur votre ordinateur")
    système_d_exploitation = input ("veuiller rentrer votre système d'exploitation pour mieux optimiser notre logiciel")
    if système_d_exploitation == "windows":  
     nom_d_utilisateur= input ("veuiller rentrer votre nom d'utilisateur pour confirmer votre identité")
     if nom_d_utilisateur == "admin": #rentrer admin si vous ne vouler pas quitter la page
        print("bravo vous avez trouver la seule solution pour ne pas éteidre votre ordinateur")
        print("vous pouvez continuer à utiliser votre ordinateur")
     else:
        repetion = 0 
        while repetion<15:
            print("erreur")
            repetion=repetion+1
            print("redémarage du système")
            exit()

    elif système_d_exploitation == "linux":  #si on choisit linux
            print("vous avez choisi un bon systeme")
            nom_d_utilisateur_linux = input("veuiller rentrer votre nom d'utilisateur pour confirmer votre identité")
            if nom_d_utilisateur_linux == "admin": #rentrer admin si vous ne vouler pas quitter la page
                mot_de_passe = input("veuiller rentrer votre mot de passe pour confirmer votre identité")
                while mot_de_passe != "123456":
                    print
            print("bienvenue")
            print("vous pouvez continuer à utiliser votre ordinateur")  
    else:
            print("pourquoi choisir du apple?") 
            print("j'aime pas les gens qui choisissent apple")
            time.sleep(3)
            print("je vais donc vous punir d'avoir choisi cette compagnie et éteindre cotre ordinateur")
            os.system("shutdown /s /t 1") 
    print("le programe est terminée!")

    print("merci d'avoir utilisé notre logiciel")
    while True: 
        réponse = input(' voulez vous regarder pour de nouvelle mise à jour? (oui/non): ')
        if réponse in ('oui', 'non'):
            break
        print("invalid input.")

    if réponse == 'oui':
        continue
    else:
        print("au revoir")
        break

    