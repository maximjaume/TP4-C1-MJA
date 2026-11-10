# APP 2026-2027 -- TP4

## Support de cours

[Support de cours au format Google docs](https://docs.google.com/presentation/d/1g-4Mm9GoIBfN_5NJ7VnbzEkx7wgbTnpe1e0VzgFyFf4/)

## Objectifs du TP4 

- Implémenter des parcours de l'arbre de calculs à la volée pour résoudre le problème du *compte est bon* : 
    - parcours en profondeur d'abord itératif
    - parcours en profondeur d'abord récursif
    - parcours en largeur d'abord itératif
- Comparer leurs efficacités
- Proposer et implémenter des améliorations

## Exercice 1 : Présentation du code fourni

Les types abstraits de données présentés au TD3 se trouvent dans le répertoire `TAD`. 
Il faut considérer les fichiers de ce répertoire comme autant de librairies de fonctions 
que vous pourrez utiliser pour vos futurs programmes :  

- `listes_doublement_chainees.py` : implémentation des listes simplement chaînées 
- `listes_simplement_chainees.py` : implémentation des listes doublement chaînées avec pointeurs de queue
- `piles_listes_python.py` : implémentation des piles à l'aide de listes python 
- `piles_listes_simplement_chainees.py` : implémentation des piles à l'aide de listes simplement chaînées
- `files_listes_python.py` :  : implémentation des files à l'aide de listes python
- `files_listes_doublement_chainees.py` : implémentation des files à l'aide de listes doublement chaînées

Le répertoire du dépôt contient les fichiers nécessaires à la réalisation du TP4 : 

- `notation_polonaise_inverse.py` : implémentation des fonctions `eval_NPI_liste(liste_expression,bool_afficher_calculs)` et `eval_NPI_file(file_expression, bool_afficher_calculs)` 
- `generer_probleme.py` : programme de génération de problèmes du compte est bon, aléatoirement ou à l'aide des classes `possible` (un ou plusieurs calculs mènent au résultat), `impossible` (aucun calcul ne mène au résultat), ou `ardu` (une seule solution mène au résultat)
- `syntaxe.py` : présentation de quelques éléments de syntaxe qui peuvent vous être utiles pour ce TP
- `compte_est_bon.py` : programme qui lit un problème de compte est bon sur son entrée standard et appelle les fonctions de parcours du fichier 
- `recherche_compte_est_bon.py` (qui restent à écrire) pour les résoudre

1. Tester l'évaluation d'expressions NPI valides ou invalides à l'aide du programme `notation_polonaise_inverse.py`, en affichant les calculs intermédiaires ou non 
- Tester chacun des appels possibles au programme `generer_probleme.py` : 
    - `./generer_probleme.py` : Génère un problème au hasard sur la sortie standard au format C1 C2 C3 C4 C5 C6 CIBLE
    - `./generer_probleme.py seed`  : Génère un problème en initialisant le générateur aléatoire avec la graine fournie
    - `./generer_probleme.py possible` : Génère un problème ayant une solution
    - `./generer_probleme.py impossible` : Génère un problème n'ayant aucune solution
    - `./generer_probleme.py ardu` : Génère un problème n'ayant qu'une seule solution
- Tester les redirections permettant de commencer la résolution du problème du compte est bon : 
    - `echo 3 5 7 9 25 50 859  | ./compteestbon.py`
    - `./generer_probleme.py 2026 | ./compteestbon.py`


## Exercice 2 : Résolution du problème du compte est bon 

Les fonctions de parcours à implémenter se trouvent dans le fichier `recherche_compte_est_bon.py`. Ce fichier contient 3 fonctions de parcours de l'arbre de calculs à la volée : 
    - `parcours_DFS(cartons, cible)` : réalise un parcours itératif en profondeur d'abord
    - `parcours_BFS(cartons, cible)` : réalise un parcours itératif en largeur d'abord
    - `parcours_DFS_recursif(choisis, restants, cible)` : réalise un parcours récursif en profondeur d'abord

Chaque fonction doit parcourir l'arbre de calculs à la recherche de la cible à partir des cartons fournis en paramètre. 
Lors du parcours, chaque fois que la fonction se rapproche de la cible, le calcul correspondant doit être affiché. 
Le parcours doit s'arrêter dès que la cible a été atteinte. 
La fonction doit renvoyer le nombre de noeuds (valides ou invalides) parcourus et l’expression NPI correspondant à la meilleure solution trouvée.

2. Implémenter chacune des fonctions de parcours de l'arbre de calculs, en proposant des améliorations permettant par exemple : 
- d'éviter de construire des expressions invalides 
- d'éviter de produire des expressions redondantes 
- de raccourcir la durée d’évaluation 

## Exercice 3 : Analyse et production d'un rapport 

3. Une fois les fonctions réalisées, mettre en oeuvre une évaluation expérimentale des parcours pour plusieurs types de problèmes :
- Le problème correpondant à votre date de naissance, par exemple `./generer_probleme.py 17081936`
- Un problème impossible : `./generer_probleme.py impossible`
- Un problème ardu : `./generer_probleme.py ardu`

4. À l'occasion de la résolution de ces problèmes, collectez les données suivantes : 
- Quelle est la taille max de la pile lors du parcours DFS ?
- Quelle est la taille max de la file lors du parcours BFS ?
- Quelle est la hauteur max de l’arbre ?
- Quelle est la largeur max de l’arbre ?
- Combien de noeuds sont parcourus (évalués) ?
- Combien de temps votre programme met-il pour afficher sa réponse avec chaque parcours ?
- Quel parcours est le plus efficace ?
