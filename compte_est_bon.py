#! /usr/bin/env python3

"""
Ce programme prendra sur son entrée standard les 6 cartons tirés au sort suivis du nombre à
trouver. Par exemple, si les cartons tirés sont 3 5 7 9 25 50 et que le nombre à découvrir est
859, il devra être appelé ainsi : echo 3 5 7 9 25 50 859  | ./compteestbon.py 
"""

from recherche_compte_est_bon import *
import sys
import time

def lire_stdin():
    """Lit l'entrée standard en invitant l'utilisateur à l'aide d'un message si le flux d'entrée n'est pas redirigé"""
    if sys.stdin.isatty():
        sys.stderr.write("Saisissez du texte (Ctrl+D pour terminer) :\n")
    return sys.stdin.read()

if __name__ == "__main__":
    cartons_nombre = lire_stdin()
    *cartons,nombre = map(int, cartons_nombre.split())
    print(f"Recherche de {nombre} avec {cartons}")
    
    debut = time.perf_counter()
    parcours_DFS(cartons, nombre)
    fin = time.perf_counter()
    print(f"DFS : {fin - debut:.6f} s")

    debut = time.perf_counter()
    parcours_DFS_recursif(cartons, nombre)
    fin = time.perf_counter()
    print(f"DFS récursif : {fin - debut:.6f} s")

    debut = time.perf_counter()
    parcours_BFS(cartons, nombre)
    fin = time.perf_counter()
    print(f"BFS : {fin - debut:.6f} s")


    
