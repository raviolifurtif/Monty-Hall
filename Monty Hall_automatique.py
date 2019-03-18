# -*-coding: utf-8 -*

import os
import random

continuer = True

while continuer == True:

    print("Bienvenue dans ce jeu de Monty Hall !")

    #initialisation du compte des parties jouées
    parties_total = 0
    parties_avec_changement = 0
    victoires_avec_changement = 0
    parties_sans_changement = 0
    victoires_sans_changement = 0

    choix_iteration = ""
    #Récupération de l'itération souhaitée par l'utilisateur
    while choix_iteration == "":
        print("\nNous allons simuler n jeux de Monty Hall dans chaque cas (changement de porte ou non)")
        choix_iteration = input("Votre choix pour n : ")
        try :
            choix_iteration = int(choix_iteration)
            if choix_iteration < 1:
                choix_iteration = ""
        except ValueError:
            choix_iteration = ""
            

    #Parties où l'on change de porte systématiquement
    for i in range(choix_iteration):

        #choix pseudo-aléatoire de la porte gagnante ainsi que de la porte choisie par le joueur
        porte_voiture = random.randrange(1,4)
        choix_porte = random.randrange(1,4)
    
        if porte_voiture != choix_porte: #Si on avait initialement choisi une porte non gagnante, alors changer de porte nous garantit la victoire
            victoires_avec_changement += 1
        
        parties_avec_changement +=1


    #Parties où l'on garde la porte initiale systématiquement
    for i in range(choix_iteration):

        #choix pseudo-aléatoire de la porte gagnante ainsi que de la porte choisie par le joueur
        porte_voiture = random.randrange(1,4)
        choix_porte = random.randrange(1,4)
    
        if porte_voiture == choix_porte: #Si on avait initialement choisi la bonne porte, c'est donc une victoire
            victoires_sans_changement += 1
        
        parties_sans_changement +=1
    
    #Affichage des statistiques actualisées
    print("\n=================================\nStatistiques :")
    print("pourcentage de victoire en changeant de porte : {}%  ({} parties jouées)".format(round(100*victoires_avec_changement/parties_avec_changement,2),parties_avec_changement))
    print("pourcentage de victoire sans changer de porte : {}%  ({} parties jouées)".format(round(100*victoires_sans_changement/parties_sans_changement,2),parties_sans_changement))
    print("=================================")
    
    quitter = ""
    while quitter == "":
        quitter = input("\nVoulez-vous refaire une simulation ? (o/n) ")
        if quitter.lower() == "o":
            pass
        elif quitter.lower() == "n":
            continuer = False
        else:
            quitter = ""


print("\nA bientôt !")

os.system("pause")
