
from TAD.piles_listes_python import Pile
from TAD.files_listes_python import File
from notation_polonaise_inverse import *


def operations_possibles(a, b):
    """Renvoie les opérations autorisées entre a et b."""
    ops = [
        (a + b, '+'),
        (a * b, '*')
    ]

    if a > b:
        ops.append((a - b, '-'))
    elif b > a:
        ops.append((b - a, '-'))

    if b != 0 and a % b == 0:
        ops.append((a // b, '/'))

    if a != 0 and b % a == 0:
        ops.append((b // a, '/'))

    # Évite les opérations donnant exactement le même résultat
    return list(dict.fromkeys(ops))


def creer_enfants(cartons):
    """
    Construit les états fils d'un état.

    Chaque carton est représenté par :
        (valeur, expression_NPI)
    """
    n = len(cartons)

    for i in range(n):
        for j in range(i + 1, n):

            a, expr_a = cartons[i]
            b, expr_b = cartons[j]

            restants = [
                cartons[k]
                for k in range(n)
                if k != i and k != j
            ]

            for resultat, operation in operations_possibles(a, b):

                # Construction correcte de l'expression NPI
                nouvelle_expr = expr_a + expr_b + [operation]

                nouveaux_cartons = restants + [
                    (resultat, nouvelle_expr)
                ]

                yield nouveaux_cartons


def cle_etat(cartons):
    """Clé permettant de reconnaître les états équivalents."""
    return tuple(sorted(valeur for valeur, expr in cartons))


def parcours_DFS(cartons, cible):
    """Parcours itératif en profondeur d'abord."""

    nb_noeuds = 0
    meilleure_expression = []
    ecart_min = float('inf')

    # Initialisation : chaque carton possède sa propre expression
    depart = [(x, [x]) for x in cartons]

    pile = Pile()
    pile.empiler(depart)

    vus = {cle_etat(depart)}

    while not pile.est_vide():

        etat = pile.depiler()
        nb_noeuds += 1

        # Évaluation des solutions disponibles dans cet état
        for valeur, expression in etat:

            ecart = abs(valeur - cible)

            if ecart < ecart_min:
                ecart_min = ecart
                meilleure_expression = expression[:]

                # Affichage des nouveaux meilleurs calculs
                print("Nouvelle meilleure solution :")
                eval_NPI_liste(expression, True)

            if ecart == 0:
                return nb_noeuds, meilleure_expression

        # Construction et empilement des états fils
        for enfant in creer_enfants(etat):

            cle = cle_etat(enfant)

            if cle not in vus:
                vus.add(cle)
                pile.empiler(enfant)

    return nb_noeuds, meilleure_expression


def parcours_BFS(cartons, cible):
    """Parcours itératif en largeur d'abord."""

    nb_noeuds = 0
    meilleure_expression = []
    ecart_min = float('inf')

    depart = [(x, [x]) for x in cartons]

    file = File()
    file.enfiler(depart)

    vus = {cle_etat(depart)}

    while not file.est_vide():

        etat = file.defiler()
        nb_noeuds += 1

        # Évaluation des solutions disponibles
        for valeur, expression in etat:

            ecart = abs(valeur - cible)

            if ecart < ecart_min:
                ecart_min = ecart
                meilleure_expression = expression[:]

                print("Nouvelle meilleure solution :")
                eval_NPI_liste(expression, True)

            if ecart == 0:
                return nb_noeuds, meilleure_expression

        # Construction et ajout des états fils
        for enfant in creer_enfants(etat):

            cle = cle_etat(enfant)

            if cle not in vus:
                vus.add(cle)
                file.enfiler(enfant)

    return nb_noeuds, meilleure_expression


def parcours_DFS_recursif(cartons, cible):
    """Parcours récursif en profondeur d'abord."""

    meilleure_expression = []
    ecart_min = float('inf')
    nb_noeuds = 0

    depart = [(x, [x]) for x in cartons]

    vus = {cle_etat(depart)}

    def parcours_aux(etat):

        nonlocal meilleure_expression
        nonlocal ecart_min
        nonlocal nb_noeuds

        nb_noeuds += 1

        # Évaluation des solutions disponibles
        for valeur, expression in etat:

            ecart = abs(valeur - cible)

            if ecart < ecart_min:
                ecart_min = ecart
                meilleure_expression = expression[:]

                print("Nouvelle meilleure solution :")
                eval_NPI_liste(expression, True)

            if ecart == 0:
                return True

        # Exploration récursive des états fils
        for enfant in creer_enfants(etat):

            cle = cle_etat(enfant)

            if cle not in vus:

                vus.add(cle)

                if parcours_aux(enfant):
                    return True

        return False

    parcours_aux(depart)

    return nb_noeuds, meilleure_expression


if __name__ == "__main__":

    cartons = [3, 5, 7, 9, 25, 50]
    cible = 859

    print("\n===== DFS ITERATIF =====")
    nb, expr = parcours_DFS(cartons, cible)
    print("Nombre de noeuds :", nb)
    print("Expression :", expr)

    print("\n===== BFS ITERATIF =====")
    nb, expr = parcours_BFS(cartons, cible)
    print("Nombre de noeuds :", nb)
    print("Expression :", expr)

    print("\n===== DFS RECURSIF =====")
    nb, expr = parcours_DFS_recursif(cartons, cible)
    print("Nombre de noeuds :", nb)
    print("Expression :", expr)
