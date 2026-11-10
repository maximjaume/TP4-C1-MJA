#! /usr/bin/env python3

"""Évaluation d’une expression NPI fournie dans une liste python ou comme une file d'opérateurs"""

from TAD.piles_listes_python import Pile
from TAD.files_listes_python import File
#from TAD.piles_listes_simplement_chainees import Pile
#from TAD.files_listes_doublement_chainees import File

def eval_NPI_file(fileExpression, afficher=False):
    # Cette fonction renvoie un tuple(BoolExpressionValide, ValeurOuNone)
    # à partir d'une file d'opérateurs et d'opérandes
    # renvoyer (False,None) signifie que l'expression n'est pas valide 
    # renvoyer (True,None) signifie que l'expression est valide, 
    # mais qu'elle ne correspond pas à un résultat calculable car elle est incomplète
    # renvoyer (True, Entier) signifie que l'expression est valide, 
    # et que son évaluation donne Entier comme résultat
    pile = Pile(); 
    while (not fileExpression.est_vide()) : 
        nextO = fileExpression.defiler()
        match nextO : 
            case '+' : 
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                pile.empiler(op1+op2)
                if (afficher) : print(op1, '+', op2, '=', op1+op2)
            case '-' : 
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                if (op2-op1<1) : return (False,None) #interdiction des résultats nuls ou négatifs 
                pile.empiler(op2-op1)
                if (afficher) : print(op2, '-', op1, '=', op2-op1)
            case '/' : 
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if (op1==0) : return (False,None)
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                if (op2 % op1 != 0) : return (False,None)
                pile.empiler(op2//op1)
                if (afficher) : print(op2, '/', op1, '=', op2//op1)
            case '*' :
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                pile.empiler(op1*op2)
                if (afficher) : print(op2, '*', op1, '=', op2*op1)
            case _ :  
                pile.empiler(nextO) 
    if (pile.longueur() ==1) : return (True, pile.sommet())
    else : return (True, None) 
   

def eval_NPI_liste(listeExpression, afficher = False):
    # Cette fonction renvoie un tuple(BoolExpressionValide, ValeurOuNone)
    # à partir d'une liste d'opérateurs et d'opérandes
    # renvoyer (False,None) signifie que l'expression n'est pas valide 
    # renvoyer (True,None) signifie que l'expression est valide, 
    # mais qu'elle ne correspond pas à un résultat calculable car elle est incomplète
    # renvoyer (True, Entier) signifie que l'expression est valide, 
    # et que son évaluation donne Entier comme résultat
    pile = Pile(); 
    for nextO in listeExpression: 
        match nextO : 
            case '+' : 
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                pile.empiler(op1+op2)
                if (afficher) : print(op1, '+', op2, '=', op1+op2)
            case '-' : 
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                if (op2-op1<1) : return (False,None) #interdiction des résultats nuls ou négatifs 
                pile.empiler(op2-op1)
                if (afficher) : print(op2, '-', op1, '=', op2-op1)
            case '/' : 
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if (op1==0) : return (False,None)
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                if (op2 % op1 != 0) : return (False,None)
                pile.empiler(op2//op1)
                if (afficher) : print(op2, '/', op1, '=', op2//op1)
            case '*' :
                if pile.est_vide() : return (False,None)
                op1 = pile.depiler()
                if pile.est_vide() : return (False,None)
                op2 = pile.depiler()
                pile.empiler(op1*op2)
                if (afficher) : print(op2, '*', op1, '=', op2*op1)
            case _ : 
                pile.empiler(nextO)
    if (pile.longueur() ==1) : return (True, pile.sommet())
    else : return (True, None)



if __name__ == "__main__":
    e1 = File() 
    e1.enfiler(3);
    e1.enfiler(1);
    e1.enfiler('-');
    print("Evaluation de 3 1 -")
    print(eval_NPI_file(e1, True));

    e2 = [1,2,'+',4,'*',5,'+']
    print("Evaluation de 1 2 + 4 * 5 +")
    print(eval_NPI_liste(e2, True))

    e3 = [1,'+',4]
    print("Evaluation de 1 + 4")
    print(eval_NPI_liste(e3, True))

    e4 = [1,2,'+',4]
    print("Evaluation de 1 2 + 4")
    print(eval_NPI_liste(e4, True))
