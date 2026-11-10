#! /usr/bin/env python3

"""Implémentation des piles à l'aide de listes simplement chainées """

from listes_simplement_chainees import ListeChainee

class Pile:
    
    def __init__(self, n=""): 
        self.data = ListeChainee(n)

    def est_vide(self): return self.data.est_vide()
    
    def sommet(self):
        if self.data.est_vide() : raise IndexError("pile vide")
        return self.data.cellule_tete().valeur

    def empiler(self, x): self.data.inserer_tete(x)
    
    def depiler(self):
        if self.data.est_vide() : raise IndexError("pile vide")
        sommet = self.data.cellule_tete().valeur
        self.data.supprimer_tete()
        return sommet
    
    def longueur(self): return self.data.longueur()
    
    def afficher(self):
        self.data.afficher()

if __name__ == "__main__":
    p1 = Pile("P1")
    p1.empiler(1)
    p1.empiler(2)
    p1.empiler(3)
    p1. afficher()
    
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    v = p1.depiler(); print("Extrait : " + str(v))
    p1. afficher()

