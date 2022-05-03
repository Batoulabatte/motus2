import random
from troll import *             #toutes les données du fichier easter egg sont importées



historiqueCode = []
historiqueCouleur = []
historiqueDaltonier = []

def comparer(proposition, secret):
    position = 0
    reponse = ""                                        #Version de base
    reponseColor = []                                   #Version avec couleur : création d'un tableau
    reponseDaltonnien = []                              #Version daltonienne : création d'un tableau
    for index in range(len(secret)):                    #la boucle for va parcourir tous les éléments de la chaine de caractères jusqu'a len(secret)
        if proposition[index] == secret[index]:
            reponse += "o"                              #lettre présente et bien placée
            reponseColor.append("🟩")
            reponseDaltonnien.append("🟧")
        elif proposition[index] in secret:
            reponse += "+"                              #lettre présente mais mal placée
            reponseColor.append("🟨")
            reponseDaltonnien.append("🟦")
        else:
            reponse += "x"                              #lettre non comprise dans le mot
            reponseColor.append("■")               #alt + 254 pour le carré noir car problème d'affichage avec cet emoji
            reponseDaltonnien.append("■")
    print(reponse)
    print("Version en couleur : ", reponseColor)
    print("Version daltonienne : ", reponseDaltonnien)
    historiqueCode.append(reponse)
    historiqueCouleur.append(reponseColor)
    historiqueDaltonier.append(reponseDaltonnien)
    if (reponse == "oooooo"):
        return True
    else:
        return False

def tour(secret, lexique):
    proposition = ""
    while proposition not in lexique:
        print("Votre mot doit contenir 6 caractères et etre dans le lexique : ")
        proposition = input("Entrez un mot de 6 lettres: ")
    proposition = proposition.lower()
    return comparer(proposition, secret)

def partie(lexique):
    nbEssais = 6
    wordlist = []
    for word in lexique:
        wordlist.append(word.strip())           #permet d'espacer les mots du lexique entre
    secret = random.choice(wordlist)
    print("Mot à deviner selectionné. \n La partie va commencer.")
    endGame = False
    print(secret)
    while endGame != True:
        endGame = tour(secret, wordlist)        #appel de la fonction tour qui retourne true si la partie est finie, sinon false
        if endGame == False:
            print("Dommage, c'est raté ! Il te reste ",  (nbEssais - 1), " essais")
        nbEssais = nbEssais - 1
        if nbEssais == 0:
            break                               #Force la sortie de la boucle while si le nombre d'essais est égal à 0
    if endGame == True:
        print("Bien joué vous avez trouver le mot en ", nbEssais, " essais")
        gigaChad()
    else:
        print("Perdu, vous avez atteint  la limite d'essais !")
        print("Le mot était ", secret)
        print("Voici votre historique d'essais : \n Version code : ", historiqueCode, "\n Version couleur : ", historiqueCouleur, "\n Version daltonien : ", historiqueDaltonier)
        shrek()

def gameInit():
    lexique = open("lexique.txt")
    partie(lexique)       #appelle la partie lexique