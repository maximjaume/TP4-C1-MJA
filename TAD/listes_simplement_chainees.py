#! /usr/bin/env python3

"""Listes simplement chaînées

TODO : 
Produire une version récursive de la fonction d’affichage 
Produire des fonctions calculant la taille de la liste en versions itératives et récursives
Tester pour des listes de taille vide, réduite à un élément ou plus longues
[BONUS] Permettre de pouvoir donner un nom à une liste
[BONUS] Ajouter un compteur permettant de savoir le nombre total de cellules produites pour gérer toutes les listes construites
    
"""

class Cellule:

    def __init__(self, val, suiv=None):
        self.valeur = val   
        self.suivant = suiv

class ListeChainee:
    def __init__(self, n="L_inconnue"):
        self.tete = None
        self.nom = n 

    @staticmethod
    def val_or_none(s):
        if s is None : return "None"
        else : return s.valeur

    def changer_nom(self,n): 
        self.nom = n
    
    def presenter_nom(self,msg): 
        # affiche un message suivi de <Nom> :
        print(f"{msg}{self.nom} : ", end="")

    def est_vide(self):
        return self.tete is None

    
    # Nombre de cellules en version itérative
    def longueur(self):
        if self.tete is None: 
            return 0
        else : 
            taille=0
            cell = self.tete
            while (cell is not None) : 
                taille += 1
                cell = cell.suivant
            return taille

    # Nombre de cellules en version récursive
    def longueur_recursif(self):
        def longueur_rec(cell): 
            # ordre de la récurrence ?  Le nombre de mailles de la liste
            # cas de base ? Cellule None
            if cell is None:
                return 0
            else :  # cas général ?
                return 1 + longueur_rec(cell.suivant)
                
        if self.tete is None: 
            return 0
        else :
            return longueur_rec(self.tete)   
    
    def afficher(self):
        self.presenter_nom("")
        if self.tete is None: 
            print("vide !")
        else:            
            courant = self.tete
            while courant is not None:
                print(courant.valeur, end=" -> ")
                courant = courant.suivant
            print("None")

    def afficher_recursif(self):
        def afficher_aux(cell) : 
            # ordre de la récurrence ? Nombre de cellules 
            # cas de base ? Cellule None
            if cell is None: 
                print("None")
            else : # cas général ?
                print(f"{cell.valeur} -> ", end="")
                afficher_aux(cell.suivant)

        self.presenter_nom("")
        if self.tete is None: 
            print("Liste vide !")
        else:
            afficher_aux(self.tete)

    def cellule_tete(self):
        return self.tete

    def cellule_queue(self) :
        cell = self.tete
        if cell is None :
            return None
        else : 
            while cell.suivant is not None:  
                cell = cell.suivant
            return cell
        
    def acces(self, i):
        if self.tete is None: 
            return None
        else : 
            index = 0
            cell = self.tete
            while (index != i) and (cell is not None) :
                index += 1 
                cell = cell.suivant
            if index == i : return cell 
            else : return None  

    def rechercher(self,val): 
        # renvoie la première occurence ou None 
        # Liste × Élément → Cellule
        if self.tete is None: 
            return None
        else : 
            cell = self.tete
            while  (cell is not None) and (cell.valeur != val) :
                cell = cell.suivant
            if cell is None : return None 
            else : return cell    

    def inserer_position(self, i, val) : 
        #Liste × int × Élément → None

        if i <= 0 : 
            # On insère en tête
            self.inserer_tete(val)
        else : 
            # On insère dans la liste 
            cell_precedente = self.acces(i-1)
            if cell_precedente is None: 
                # On insère en queue 
                self.inserer_queue(val)
            else : 
                nouvelle = Cellule(val,cell_precedente.suivant)
                cell_precedente.suivant = nouvelle

    def inserer_tete(self, val):
        nouvelle = Cellule(val, self.tete) 
        self.tete = nouvelle

    def inserer_queue(self, val):
        nouvelle = Cellule(val)

        # On n'a pas de pointeur sur la queue, on doit trouver la dernière maille pour la chainer avec nouvelle
        lastM = self.tete
        if lastM is None: 
            self.tete = nouvelle
        else : 
            while lastM.suivant is not None: 
                lastM = lastM.suivant
            # ici lastM dénote la dernière cellule ! 
            lastM.suivant = nouvelle

    def inserer_queue_recursif(self, val):
        def inserer_queue_aux(cell, val) : 
            if cell.suivant is None : 
                cell.suivant = Cellule(val)
            else : 
                inserer_queue_aux(cell.suivant, val)
        if self.tete is not None : 
            inserer_queue_aux(self.tete, val)
        else : 
            self.tete = Cellule(val)

    def inserer_avant(self, cell, val) : 
        # Cellule × Élément → None
        if cell is not None:
            if cell is self.tete : 
                self.tete = Cellule(val,cell)
            else :
                # Il faut trouver la cellule precedent cell 
                cell_precedente = self.tete
                while  (cell_precedente is not None) and (cell_precedente.suivant is not cell) :
                    cell_precedente = cell_precedente.suivant
                if cell_precedente is not None :
                    if cell_precedente.suivant is cell :
                        cell_precedente.suivant = Cellule(val,cell)

    def inserer_apres(self, cell, val) : 
        # Cellule × Élément → None
        if cell is not None: 
            cell.suivant = Cellule(val,cell.suivant)

    def supprimer_position(self, i) : 
        # Liste × int → None   
        if i <= 0 : 
            # On supprime en tête
            self.supprimer_tete()
        else : 
            # On supprime dans la liste apres la cellule d'indice i-1
            cell_precedente = self.acces(i-1)
            if cell_precedente is not None:
                if cell_precedente.suivant is not None:
                    cell_precedente.suivant = cell_precedente.suivant.suivant
                # else : # La position i n'existe pas : rien à faire  
            # else : # Rien à supprimer 


    def supprimer_tete(self):      
        if self.tete is not None: 
            seconde = self.tete.suivant
            self.tete = seconde


    def supprimer_queue(self):      
        if self.tete is not None :
            avantLastM = self.tete
            if avantLastM.suivant is None : # il n'y avait qu'une seule cellule : on la supprime
                self.tete = None 
            else :
                lastM = avantLastM.suivant 
                while lastM.suivant is not None: 
                    avantLastM = lastM
                    lastM = lastM.suivant
                # ici lastM dénote la dernière cellule qu'il faut supprimer !
                avantLastM.suivant = None
    
    def supprimer_queue_recursif(self):
        def supprimer_queue_aux(avantCell, cell): 
            # Hyp : avantCell n'est pas none
            if cell.suivant is not None: 
                supprimer_queue_aux(avantCell.suivant, cell.suivant)
            else : 
                # cell.suivant est None, donc cell est la dernière cellule qu'il faut supprimer
                avantCell.suivant = None
        
        if self.tete is not None :
            if self.tete.suivant is None : # il n'y avait qu'une seule cellule : on la supprime
                self.tete = None 
            else :
                # self.tete et self.tete.suivant ne sont pas nuls
                supprimer_queue_aux(self.tete, self.tete.suivant)
def tests():

    print("\n========== TESTS DES LISTES SIMPLEMENT CHAÎNÉES ==========")

    # --------------------------------------------------
    # 1. Création et initialisation
    # --------------------------------------------------

    print("\n--- 1. CRÉATION DES LISTES ---")

    L = ListeChainee("L")
    L1 = ListeChainee("L1")
    L2 = ListeChainee("L2")

    L.inserer_tete(10)
    L.inserer_tete(20)
    L.inserer_tete(30)

    L1.inserer_tete(10)

    L.afficher()
    L1.afficher()
    L2.afficher()

    # --------------------------------------------------
    # 2. Tests des insertions en position
    # --------------------------------------------------

    print("\n--- 2. INSERTIONS EN POSITION ---")

    L1.inserer_position(0, 5)
    L1.afficher()

    L1.inserer_position(2, 15)
    L1.afficher()

    L1.inserer_position(3, 20)
    L1.afficher()

    # Insertion à une position supérieure à la longueur
    L1.inserer_position(10, 25)
    L1.afficher()

    # --------------------------------------------------
    # 3. Tests de acces()
    # --------------------------------------------------

    print("\n--- 3. ACCÈS AUX CELLULES ---")

    for i in [-1, 0, 1, 2, 3, 10]:
        L.presenter_nom(f"Cellule d'indice {i}")
        print(ListeChainee.val_or_none(L.acces(i)))

    # --------------------------------------------------
    # 4. Tests de rechercher()
    # --------------------------------------------------

    print("\n--- 4. RECHERCHE D'UNE VALEUR ---")

    for val in [0, 10, 20, 30, 2, 3]:
        L.presenter_nom(f"Recherche de {val}")
        print(ListeChainee.val_or_none(L.rechercher(val)))

    # --------------------------------------------------
    # 5. Tests des longueurs et affichages
    # --------------------------------------------------

    print("\n--- 5. LONGUEUR ET AFFICHAGE ---")

    for liste in [L, L1, L2]:
        liste.afficher()
        liste.afficher_recursif()

        liste.presenter_nom("Longueur itérative")
        print(liste.longueur())

        liste.presenter_nom("Longueur récursive")
        print(liste.longueur_recursif())

    # --------------------------------------------------
    # 6. Tests d'insertion avant et après une cellule
    # --------------------------------------------------

    print("\n--- 6. INSERTIONS AVANT ET APRÈS ---")

    L3 = ListeChainee("L3")

    for val in [10, 20, 30]:
        L3.inserer_queue(val)

    L3.afficher()

    # Avant la tête
    L3.inserer_avant(L3.cellule_tete(), 5)
    L3.afficher()

    # Avant une cellule du milieu
    L3.inserer_avant(L3.acces(2), 15)
    L3.afficher()

    # Après une cellule du milieu
    L3.inserer_apres(L3.acces(2), 17)
    L3.afficher()

    # Après la queue
    L3.inserer_apres(L3.cellule_queue(), 40)
    L3.afficher()

    # --------------------------------------------------
    # 7. Tests de suppression en position
    # --------------------------------------------------

    print("\n--- 7. SUPPRESSIONS EN POSITION ---")

    L4 = ListeChainee("L4")

    for val in [10, 20, 30, 40, 50]:
        L4.inserer_queue(val)

    L4.afficher()

    # Suppression en tête
    L4.supprimer_position(0)
    L4.afficher()

    # Suppression au milieu
    L4.supprimer_position(1)
    L4.afficher()

    # Suppression en queue
    L4.supprimer_position(2)
    L4.afficher()

    # Suppression à une position inexistante
    L4.supprimer_position(10)
    L4.afficher()

    # Suppression de tous les éléments restants
    L4.supprimer_position(0)
    L4.supprimer_position(0)
    L4.afficher()

    # --------------------------------------------------
    # 8. Tests de suppression en tête et en queue
    # --------------------------------------------------

    print("\n--- 8. SUPPRESSIONS EN TÊTE ET EN QUEUE ---")

    L5 = ListeChainee("L5")

    # Suppression dans une liste vide
    L5.supprimer_tete()
    L5.supprimer_queue()
    L5.afficher()

    # Suppression de l'unique élément par la queue
    L5.inserer_tete(100)
    L5.supprimer_queue()
    L5.afficher()

    # Réinsertion après vidage
    L5.inserer_queue(200)
    L5.afficher()

    # Suppression de l'unique élément par la tête
    L5.supprimer_tete()
    L5.afficher()

    # --------------------------------------------------
    # 9. Tests des insertions en tête et en queue
    # --------------------------------------------------

    print("\n--- 9. INSERTIONS EN TÊTE ET EN QUEUE ---")

    L6 = ListeChainee("L6")

    L6.inserer_tete(10)
    L6.afficher()

    L6.inserer_tete(20)
    L6.afficher()

    L6.inserer_queue(30)
    L6.afficher()

    L6.inserer_queue(40)
    L6.afficher()

    # --------------------------------------------------
    # 10. Tests des versions récursives
    # --------------------------------------------------

    print("\n--- 10. INSERTIONS ET SUPPRESSIONS RÉCURSIVES ---")

    L7 = ListeChainee("L7")

    # Insertion récursive en queue
    L7.inserer_queue_recursif(10)
    L7.afficher()

    L7.inserer_queue_recursif(20)
    L7.afficher()

    L7.inserer_queue_recursif(30)
    L7.afficher()

    # Suppression récursive en queue
    L7.supprimer_queue_recursif()
    L7.afficher()

    L7.supprimer_queue_recursif()
    L7.afficher()

    L7.supprimer_queue_recursif()
    L7.afficher()

    # Suppression récursive dans une liste vide
    L7.supprimer_queue_recursif()
    L7.afficher()

    # Réinsertion après vidage
    L7.inserer_queue_recursif(100)
    L7.afficher()

    L7.inserer_queue_recursif(200)
    L7.afficher()

    # --------------------------------------------------
    # 11. Tests complémentaires de cellule_tete et cellule_queue
    # --------------------------------------------------

    print("\n--- 11. TÊTE ET QUEUE ---")

    for liste in [L, L1, L2, L3, L4, L5, L6, L7]:

        liste.presenter_nom("Cellule de tête")
        print(ListeChainee.val_or_none(liste.cellule_tete()))

        liste.presenter_nom("Cellule de queue")
        print(ListeChainee.val_or_none(liste.cellule_queue()))

    print("\n========== FIN DES TESTS ==========")


if __name__ == "__main__":
    tests()
