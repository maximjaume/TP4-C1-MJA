""" Implémentation des parcours de l’arbre de calculs à la volée :
- parcours en profondeur d’abord itératif
- parcours en profondeur d’abord récursif
- parcours en largeur d’abord itératif """

from TAD.piles_listes_python import Pile
from TAD.files_listes_python import File
from notation_polonaise_inverse import *

def operations_possibles(a, b):
    ops = []
    ops.append((a + b, '+'))
    ops.append((a * b, '*'))
    if a - b > 0:
        ops.append((a - b, '-'))
    if b - a > 0:
        ops.append((b - a, '-'))
    if b != 0 and a % b == 0:
        ops.append((a // b, '/'))
    if a != 0 and b % a == 0:
        ops.append((b // a, '/'))
    return ops

def parcours_DFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []
    ecart_min = float('inf')
    
    pile = Pile()
    pile.empiler((cartons, []))
    
    while not pile.est_vide():
        cartons_actuels, expr = pile.depiler()
        nb_noeuds += 1
        
        if len(expr) >= 3:
            res, valide = eval_NPI_liste(expr, False)
            if valide:
                ecart = abs(res - cible)
                if ecart < ecart_min:
                    ecart_min = ecart
                    meilleure_expression = expr
                if ecart == 0:
                    break
        
        n = len(cartons_actuels)
        for i in range(n):
            for j in range(i + 1, n):
                a = cartons_actuels[i]
                b = cartons_actuels[j]
                restants = [cartons_actuels[k] for k in range(n) if k != i and k != j]
                for val_res, op in operations_possibles(a, b):
                    # Stocker les nombres sous forme d'entiers (ou de chaînes selon l'attendu, mais eval_NPI_liste manipule souvent des entiers/float)
                    nouvelle_expr = expr + [a, b, op]
                    pile.empiler((restants + [val_res], nouvelle_expr))
                    
    return meilleure_expression, nb_noeuds

def parcours_BFS(cartons, cible) : 
    # cartons : une liste
    # cible : entier 
    nb_noeuds = 0
    meilleure_expression = []
    ecart_min = float('inf')
    
    file = File()
    file.enfiler((cartons, []))
    
    while not file.est_vide():
        cartons_actuels, expr = file.defiler()
        nb_noeuds += 1
        
        if len(expr) >= 3:
            res, valide = eval_NPI_liste(expr, False)
            if valide:
                ecart = abs(res - cible)
                if ecart < ecart_min:
                    ecart_min = ecart
                    meilleure_expression = expr
                if ecart == 0:
                    break
        
        n = len(cartons_actuels)
        for i in range(n):
            for j in range(i + 1, n):
                a = cartons_actuels[i]
                b = cartons_actuels[j]
                restants = [cartons_actuels[k] for k in range(n) if k != i and k != j]
                for val_res, op in operations_possibles(a, b):
                    nouvelle_expr = expr + [a, b, op]
                    file.enfiler((restants + [val_res], nouvelle_expr))
                    
    return meilleure_expression, nb_noeuds 

def parcours_DFS_recursif(cartons, cible) :
    meilleure_expression = []
    nb_noeuds = 0
    ecart_min = float('inf')

    def parcours_DFSR_aux(choisis, restants) :
        nonlocal meilleure_expression
        nonlocal nb_noeuds
        nonlocal cible
        nonlocal ecart_min
        
        nb_noeuds += 1
        
        if len(choisis) >= 3:
            res, valide = eval_NPI_liste(choisis, False)
            if valide:
                ecart = abs(res - cible)
                if ecart < ecart_min:
                    ecart_min = ecart
                    meilleure_expression = choisis
                if ecart == 0:
                    return True
        
        n = len(restants)
        for i in range(n):
            for j in range(i + 1, n):
                a = restants[i]
                b = restants[j]
                suivants = [restants[k] for k in range(n) if k != i and k != j]
                
                for val_res, op in operations_possibles(a, b):
                    nouvelle_expr = choisis + [a, b, op]
                    if parcours_DFSR_aux(nouvelle_expr, suivants + [val_res]):
                        return True
        return False
        
    # Appeler parcours_DFSR_aux ! 
    parcours_DFSR_aux([], cartons)

    return meilleure_expression, nb_noeuds


if __name__ == "__main__":
    parcours_DFS([3,5, 7, 9, 25, 50], 859)
    parcours_BFS([3,5, 7, 9, 25, 50], 859)
    parcours_DFS_recursif([3,5, 7, 9, 25, 50], 859)


