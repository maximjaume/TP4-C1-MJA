#! /usr/bin/env python3

"""
Ce programme génère un problème de compte est bon sur sa sortie standard : 
Il affiche 6 valeurs tirées au sort parmi les cartons 1 à 10 en double, 25, 50, 75 et 100,
puis génère un nombre aléatoire entre 100 et 999.

Ce programme prend un argument en ligne de commande pour initialiser le générateur aléatoire
afin de retrouver la même séquence de valeurs à chaque exécution

On peut aussi passer des mots clés comme "possible", "ardu" et "impossible" 
afin de générer des problèmes de chaque classe. 

Cf. https://orthotop.fr/le-compte-est-bon-les-comptes-impossibles pour la liste exhaustive, 
élaborée en 1996 par Frédéric Vandamme, des 1.046.714 comptes impossibles, 
c'est-à-dire des comptes irréalisables au jeu Le Compte est Bon, 
qui représentent 8,78 % des 11.918.700 tirages possibles à partir des 13 243 combinaisons possibles de 6 plaques.

Cf. https://orthotop.fr/le-compte-est-bon-les-tirages-universels
pour la liste des tirages universels, c'est-à-dire les 1 226 tirages 
pour lesquels les comptes de 100 à 999 sont tous possibles au jeu Le Compte est Bon.

Cf. https://orthotop.fr/2024/07/comptes-ardus.html
pour  une sélection une sélection de comptes à solutions uniques, 
fournie par Maître Julien Bonthoux.
"""

import random
import sys

# numero = random.randint(1, 100) 
# Cela tire un entier entre 1 et 100, bornes incluses.

UNIVERSELS = [
    [2,6,7,8,10,75],
    [2,6,7,8,10,100],
    [2,6,7,8,25,50],
    [2,6,7,8,25,75],
    [2,6,7,8,25,100],
    [2,6,7,8,50,75],
    [2,6,7,8,75,100],
    [2,6,7,9,10,25],
    [2,6,7,9,10,50],
    [2,6,7,9,10,75],
    [2,6,7,9,10,100],
    [2,6,7,9,25,50],
    [2,6,7,9,25,75],
    [2,6,7,9,25,100],
    [2,6,7,9,50,75],
    [2,6,7,9,50,100],
    [2,6,7,9,75,100],
    [2,6,7,10,25,50],
    [2,6,7,10,25,75],
    [2,6,7,10,25,100],
    [2,6,7,10,50,75],
    [2,6,7,10,50,100],
    [2,6,7,10,75,100],
    [2,6,8,8,9,100]
]

IMPOSSIBLES =[
    [7,7,8,9,9,25,365],
    [7,7,8,9,9,50,667],
    [7,7,8,9,9,75,241],
    [7,7,8,9,9,100,281],
    [7,7,8,9,10,10,362],
    [7,7,8,9,10,25,636],
    [7,7,8,9,10,50,983],
    [7,7,8,9,10,75,946],
    [7,7,8,9,25,50,964],
    [7,7,8,9,25,75,998],
    [7,7,8,9,25,100,985],
    [7,7,8,9,50,75,985],
    [7,7,8,9,50,100,989],
    [7,7,8,9,75,100,869],
    [7,7,8,10,10,25,996],
    [7,7,8,10,10,50,997],
    [7,7,8,10,10,75,995],
    [7,7,8,10,10,100,835],
    [7,7,8,10,25,50,981],
    [7,7,8,10,25,75,989],
    [7,7,8,10,25,100,439],
    [7,7,8,10,50,75,724],
    [7,7,8,10,50,100,834],
    [7,7,8,10,75,100,361]
]

ARDUS = [
    [1,4,6,25,50,100,263],
    [1,6,7,7,25,50,673],
    [1,8,8,9,9,100,356],
    [1,8,9,10,10,100,421],
    [1,9,9,10,10,100,555],
    [1,9,9,25,50,75,286],
    [1,10,25,50,75,100,559],
    [2,2,5,25,50,100,926],
    [2,3,3,25,50,75,489],
    [2,3,4,25,50,100,909],
    [2,3,4,50,75,100,566],
    [2,3,10,50,75,100,641],
    [2,4,7,25,50,100,741],
    [2,7,9,25,50,75,772],
    [2,10,10,25,50,75,214],
    [3,4,4,25,50,75,682],
    [3,5,5,50,75,100,409],
    [3,6,8,25,50,100,909],
    [3,7,10,10,75,100,431],
    [4,4,7,10,75,100,586],
    [5,5,10,25,50,75,341],
    [5,7,9,10,50,75,964],
    [6,7,7,25,50,75,847],
    [9,10,10,25,50,75,964]
]

CARTONS = [i+1 for i in range(10)] + [i+1 for i in range(10)] + [25,50,75,100]

def tirer_cartons_nombre() :
    cartons_choisis = [] 
    for i in range(6) : 
        indice = random.randint(0, len(CARTONS)-1)
        cartons_choisis.append(CARTONS.pop(indice))
    cartons_choisis.append(random.randint(100, 999))
    return cartons_choisis

if __name__ == "__main__":
    if len(sys.argv) == 2:
        arg = sys.argv[1]
        if arg.isdigit():
            # on initialise le générateur alétoire avec la graine fournie
            seed=int(sys.argv[1])
            random.seed(seed)
            probleme = tirer_cartons_nombre()
        else : 
            match arg : 
                case "impossible" : 
                    probleme = IMPOSSIBLES.pop(random.randint(0, len(IMPOSSIBLES)-1))
                case "ardu" : 
                    probleme = ARDUS.pop(random.randint(0, len(ARDUS)-1))
                case "possible" :
                    probleme = UNIVERSELS.pop(random.randint(0, len(UNIVERSELS)-1))
                    probleme.append(random.randint(100, 999))
                case _ : 
                    probleme = tirer_cartons_nombre()
    else : 
        probleme = tirer_cartons_nombre()

    for i in range(len(probleme)-1) : 
        print(probleme[i], end=" ")
    print(probleme[i+1])
        
