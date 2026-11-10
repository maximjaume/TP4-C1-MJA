#! /usr/bin/env python3

"""Listes doublement chaînées"""

class CelluleDoublementChainee:

    def __init__(self, val, suiv=None):
        self.valeur = val   
        self.suivant = suiv
        self.precedent = None
        if suiv is not None:
            suiv.precedent = self

class ListeDoublementChainee:
    def __init__(self, n="L_inconnue"):
        self.tete = None
        self.queue = None
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
        # if self.tete is not None: 
        #     print("Valeur en tete : " + str(self.tete.valeur))
        # else :
        #     print("Tete is None")

        # if self.queue is not None: 
        #     print("Valeur en queue : " + str(self.queue.valeur))
        # else :
        #     print("Queue is None") 

        if self.tete is None: 
            print("Liste vide !")
        else :
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

    def cellule_queue(self):
        return self.queue

    def acces(self, i):
        if self.tete is None: 
            return None
        else : 
            index = 0
            cell = self.tete
            while (index != i) and (cell != None) :
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
            while  (cell != None) and (cell.valeur != val) :
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
                nouvelle = CelluleDoublementChainee(val,cell_precedente.suivant)
                nouvelle.precedent = cell_precedente
                cell_precedente.suivant = nouvelle
                if nouvelle.suivant is None: 
                    self.queue = nouvelle

    # Ajouter en début sans oublier le double chainage et le pointeur de queue
    def inserer_tete(self, val):
        nouvelle = CelluleDoublementChainee(val, self.tete)

        # Si c'est la première cellule créée, on doit donner une valeur à self.tete et self.queue
        # Sinon, on ne doit changer que self.tete  
        if self.tete is None: 
            self.queue = nouvelle

        self.tete = nouvelle

    def inserer_queue(self, val):
        derniere = CelluleDoublementChainee(val) #Ce sera la dernière

        # Si c'est la première cellule créée, on doit donner une valeur à self.tete et self.queue
        if self.tete is None:
            self.queue = derniere
            self.tete = derniere
        else :
            # Sinon, on doit la chainer à la dernière et changer le pointeur de queue 
            self.queue.suivant = derniere
            derniere.precedent = self.queue
            self.queue = derniere

    def inserer_avant(self, cell, val) : 
        # Cellule × Élément → None
        if cell is not None:
            ancienPrecedent = cell.precedent
            nouvelle = CelluleDoublementChainee(val,cell)
            nouvelle.precedent = ancienPrecedent
            if ancienPrecedent is not None : 
                ancienPrecedent.suivant = nouvelle
            else : 
                # cell était la première de la liste ! La nouvelle cellule devient la nouvelle tête
                self.tete = nouvelle

    def inserer_apres(self, cell, val) : 
        # Cellule × Élément → None
        if cell is not None:
            cell.suivant = CelluleDoublementChainee(val,cell.suivant)
            cell.suivant.precedent = cell
            # Attention si cell était la dernière cellule : la nouvelle  cellule devient la queue ! 
            if cell.suivant.suivant is None : 
                self.queue = cell.suivant

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
                    # On vient peut-être de supprimer la dernière cellule et donc de changer la queue 
                    if cell_precedente.suivant is None : 
                        self.queue = cell_precedente
                    else : 
                        cell_precedente.suivant.precedent = cell_precedente
                # else : # La position i n'existe pas : rien à faire  
            # else : # Rien à supprimer 

    def supprimer_tete(self):      
        if self.tete is not None: 
            seconde = self.tete.suivant
            if seconde is not None:     
                seconde.precedent = None
            else : 
                self.queue = None   # C'était la dernière cellule : il faut mettre à jour le pointeur de queue
            self.tete = seconde     # Peut valoir None ou une vraie cellule le cas échéant

    def supprimer_queue(self):      
        if self.queue is not None: 
            precedente = self.queue.precedent
            if precedente is not None:     
                precedente.suivant = None
            else : 
                self.tete = None   # C'était la dernière cellule : il faut mettre à jour le pointeur de tete
            self.queue = precedente
    

def tests(): 
    print("\n========== TESTS DES LISTES DOUBLEMENT CHAÎNÉES ==========")

    # --------------------------------------------------
    # 1. Création et initialisation
    # --------------------------------------------------

    print("\n--- 1. CRÉATION DES LISTES ---")

    L = ListeDoublementChainee("L")
    L1 = ListeDoublementChainee("L1")
    L2 = ListeDoublementChainee("L2")

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
        print(ListeDoublementChainee.val_or_none(L.acces(i)))

    # --------------------------------------------------
    # 4. Tests de rechercher()
    # --------------------------------------------------

    print("\n--- 4. RECHERCHE D'UNE VALEUR ---")

    for val in [0, 10, 20, 30, 2, 3]:
        L.presenter_nom(f"Recherche de {val}")
        print(ListeDoublementChainee.val_or_none(L.rechercher(val)))

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

    L3 = ListeDoublementChainee("L3")

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

    L4 = ListeDoublementChainee("L4")

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

    L5 = ListeDoublementChainee("L5")

    # Suppression dans une liste vide
    L5.supprimer_tete()
    L5.supprimer_queue()
    L5.supprimer_position(0)
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

    L6 = ListeDoublementChainee("L6")

    L6.inserer_tete(10)
    L6.afficher()

    L6.inserer_tete(20)
    L6.afficher()

    L6.inserer_queue(30)
    L6.afficher()

    L6.inserer_queue(40)
    L6.afficher()


    print("\n========== FIN DES TESTS ==========")


if __name__ == "__main__":
    tests()
