# Définition de la fonction Next qui prend un argument x
def Next(x) :
    # Calculer la valeur suivante à partir de x en appliquant la formule (A * x + B) modulo C
    # Le symbole * signifie la multiplication, + signifie l'addition, % est l'opérateur modulo qui donne le reste de la division
    # Cette fonction retourne le résultat calculé
    return (A * x + B) % C

# Boucle infinie qui ne s'arrêtera que lorsqu'une condition explicite de rupture (break) sera rencontrée
while True :
    # Lire une ligne de l'entrée standard, la séparer en éléments, les convertir en entiers et les assigner aux variables N, A, B, C, X
    # map applique la fonction int à chaque élément généré par input().split()
    # input() lit une ligne de texte saisie par l'utilisateur
    N, A, B, C, X = map(int, input().split())
    # Vérifier si la valeur de C est égale à 0
    # == est l'opérateur de comparaison pour l'égalité
    if(C == 0) :
        # Si C est égal à 0, quitter la boucle en utilisant break
        break
    else :
        # Sinon, continuer le traitement
        # Lire la séquence d'entiers attendue depuis l'entrée utilisateur, la convertir en liste et l'assigner à la variable Y
        Y = list(map(int, input().split()))
        # Boucle for pour répéter l'opération jusqu'à 10001 inclus (soit 10002 itérations)
        for i in range(10002) :
            # Vérifier si on a atteint la dernière itération autorisée (i == 10001)
            if(i == 10001) :
                # Si oui, afficher -1 pour signaler l'échec à trouver la solution dans la limite fixée
                print(-1)
            else :
                # Si i n'est pas égal à 10001, continuer la procédure principale
                # Vérifier si la valeur actuelle de X est égale au premier élément de la liste Y
                if(X == Y[0]) :
                    # Si c'est vrai, supprimer le premier élément de la liste Y grâce à del Y[0]
                    # Cela fait avancer la condition de succès sur les éléments de la séquence
                    del Y[0]
                # Vérifier si la liste Y est désormais vide, c'est-à-dire que tous les éléments ont été validés
                if(len(Y) == 0) :
                    # Si c'est le cas, afficher la valeur de l'itération courante i, indiquant combien il a fallu de tours pour valider la séquence
                    print(i)
                    # Sortir de la boucle for grâce à break, car le résultat est trouvé
                    break
                else :
                    # Sinon, c'est-à-dire si la liste Y n'est pas encore vide
                    # Calculer la prochaine valeur de X en appelant la fonction Next avec l'ancienne valeur de X
                    X = Next(X)