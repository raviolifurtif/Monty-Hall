# -*-coding: utf-8 -*

import os
import random
import time

print("Bienvenue dans ce jeu de Monty Hall !")

#initialisation du compte des parties jouées
parties_total = 0
parties_avec_changement = 0
victoires_avec_changement = 0
parties_sans_changement = 0
victoires_sans_changement = 0

continuer = True

#On entre dans la boucle de jeu
while continuer == True:

    #liste contenant les choix de portes possibles
    numeros = [1,2,3]
    
    #Choix pseudo-aléatoire d'une porte gagnante parmi les 3
    porte_voiture = random.randrange(1,4)
    
    print("     ———   ———   ———   ")
    print("    | ? | | ? | | ? |  ")
    print("    |   | |   | |   |  ")
    print("    | 1 | | 2 | | 3 |  ")
    print("     ———   ———   ———   ")
    print("Une voiture se trouve dernière l'une des trois portes qui vous font face.")
    print("Vous pouvez la remporter si vous deviner laquelle...")
    print("Mais attention, les deux autres cachent chacune une chèvre.")
    
    choix_porte = ""
    
    #Récupération de la porte choisie par le candidat
    while choix_porte not in numeros:
        choix_porte = input("\nQuel numéro de porte choisissez-vous ? ")
        try :
            choix_porte = int(choix_porte)
        except ValueError:
            choix_porte = ""
    
    #On enlève la porte choisie de la liste [1,2,3]
    numeros.remove(choix_porte)
    
    print("\nHum, la porte {}, très intéressant.".format(choix_porte))
    
    time.sleep(1)
    
    #Si la porte gagnante n'a pas été choisie,
    #on ouvre une des portes restantes au hasard
    if porte_voiture not in numeros: 
        porte_ouverte = random.choice(numeros)
        numeros.remove(porte_ouverte)
    #Sinon, on ouvre la porte non gagnante parmi les 2 restantes
    else :
        numeros.remove(porte_voiture)
        porte_ouverte = numeros[0]
        numeros = [porte_voiture]

    #La liste numeros contient maintenant le numéro de la porte qui n'a pas été choisie
    #et qui ne va pas être ouverte.

    print("Mais, parmi les portes restantes, je dois vous annoncer quelque chose :")
    
    time.sleep(1)
    
    print("La porte numéro {} cachait une chèvre...".format(porte_ouverte))
    
    
    time.sleep(1)
    
    
    print("\nSachant cela, souhaitez-vous changer de porte et choisir la porte numéro {} ?".format(numeros[0]))
    
    changement = ""
    
    #On demande si le joueur souhaite changer de porte
    while changement == "":
        changement = input("Tapez o pour oui, ou n pour non : ")
        if changement.lower() == "o":
            changement = True
        elif changement.lower() == "n":
            changement = False
        else : 
            changement = ""
    
    #En cas de changement, on change la porte choisie et on incrémente la variable parties_avec_changement
    if changement:
        choix_porte = numeros[0]
        parties_avec_changement += 1
        if choix_porte == porte_voiture: #Victoire
            print("\nFélicitations, vous avez gagné la voiture !!")
            victoires_avec_changement +=1
        else: #Défaite
            print("\nDommage, votre choix n'a pas payé cette fois-ci...")
    else : #En cas de non changement
        parties_sans_changement += 1
        if choix_porte == porte_voiture:
            print("\nFélicitations, vous avez gagné la voiture !!")
            victoires_sans_changement += 1
        else:
            print("\nDommage, votre choix n'a pas payé cette fois-ci...")
            
    #Affichage des scores actualisés
    if parties_avec_changement == 0:
        print("\n=================================\nStatistiques :")
        print("pourcentage de victoire en changeant de porte : 0.0%  (0 parties jouées)")
        print("pourcentage de victoire sans changer de porte : {}%  ({} parties jouées)".format(round(100*victoires_sans_changement/parties_sans_changement,2),parties_sans_changement))
        print("=================================")
    elif parties_sans_changement == 0:
        print("\n=================================\nStatistiques :")
        print("pourcentage de victoire en changeant de porte : {}%  ({} parties jouées)".format(round(100*victoires_avec_changement/parties_avec_changement,2),parties_avec_changement))
        print("pourcentage de victoire sans changer de porte : 0.0%  (0 parties jouées)")
        print("=================================")
    else:
        print("\n=================================\nStatistiques :")
        print("pourcentage de victoire en changeant de porte : {}%  ({} parties jouées)".format(round(100*victoires_avec_changement/parties_avec_changement,2),parties_avec_changement))
        print("pourcentage de victoire sans changer de porte : {}%  ({} parties jouées)".format(round(100*victoires_sans_changement/parties_sans_changement,2),parties_sans_changement))
        print("=================================")
    
    quitter = ""
    while quitter == "":
        quitter = input("\nVoulez-vous jouer à nouveau ? (o/n) ")
        if quitter.lower() == "o":
            pass
        elif quitter.lower() == "n":
            continuer = False
        else:
            quitter = ""
            
print("A bientôt !")

os.system("pause")
