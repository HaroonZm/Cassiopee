import math  # Importation du module math, qui contient des fonctions mathématiques comme 'ceil'

# Lecture de deux entiers de la saisie standard.
# La fonction input() attend une ligne de texte de l'utilisateur.
# split() découpe la ligne en éléments séparés par des espaces.
# map(int, ...) convertit chaque élément en entier.
# Les deux entiers lus sont respectivement stockés dans 'n' et 't'.
n, t = map(int, input().split())

# Création d'une liste 'h' de taille 'n', initialisée avec des zéros.
# Cela sert à stocker ultérieurement des valeurs qui remplaceront les zéros.
h = [0] * n

# Boucle 'for' qui s'exécute 'n' fois, de i=0 à i=n-1.
# Pour chaque itération, on lit un entier depuis l'entrée standard,
# qu'on place à la position i de la liste 'h'.
for i in range(n):
    h[i] = int(input())

# Création d'une nouvelle liste 't_first' de taille n+1, initialisée à zéro.
# Cette liste va contenir les sommes partielles cumulées des valeurs de 'h'.
t_first = [0] * (n + 1)

# Création d'une liste 'w' de taille n, initialisée à zéro.
# Cette liste va stocker un 'retard' ou 'dépassement' calculé plus tard.
w = [0] * n

# Affichage du résultat d'un calcul :
# (t + 0.5) / h[0] divise la quantité t + 0.5 par le premier élément de 'h'.
# math.ceil() arrondit ce résultat à l'entier supérieur.
# Ensuite, ce résultat est affiché à l'écran.
print(math.ceil((t + 0.5) / h[0]))

# On attribue à t_first[1] la valeur de h[0].
# Cela fixe la première valeur cumulative pour la suite du code.
t_first[1] = h[0]

# Boucle principale qui commence à l'index 1 jusqu'à n-1 inclus.
for i in range(1, n):

    # Si la valeur courante de t_first[i] dépasse t,
    # on affiche 1 (cela représente probablement un nombre d'actions minimal).
    if t_first[i] > t:
        print(1)
        # Mise à jour de la valeur correspondante dans t_first en y ajoutant h[i].
        t_first[i + 1] = t_first[i] + h[i]
        # On passe à l'itération suivante (continue évite d'exécuter le code du dessous).
        continue

    # Si la somme de h[i-1] et w[i-1] est supérieure à h[i] :
    if h[i - 1] + w[i - 1] > h[i]:
        # Cela signifie qu'il y a un surplus à reporter.
        # On calcule ce surplus et on le stocke dans w[i].
        w[i] = (h[i - 1] + w[i - 1]) - h[i]
        # Mise à jour de t_first avec ce nouvel élément traité.
        t_first[i + 1] = t_first[i] + h[i]

        # Calcul du temps restant à traiter (delta_t).
        delta_t = t - t_first[i]
        # Calcul du nombre d'opérations nécessaires avec arrondi supérieur.
        # On ajoute 0.5 à delta_t puis on divise par (h[i] + w[i]).
        temp = math.ceil((delta_t + 0.5) / (h[i] + w[i]))

        # Si le reste de la division delta_t / (h[i] + w[i]) dépasse ou égale h[i] :
        if delta_t % (h[i] + w[i]) >= h[i]:
            # Il faut une opération supplémentaire, donc on affiche temp + 1.
            print(temp + 1)
        else:
            # Sinon, temp suffit, on l'affiche.
            print(temp)

    else:
        # Sinon, il n'y a pas de surplus à reporter.
        # On remet w[i] à zéro.
        w[i] = 0
        # Mise à jour cumulative de t_first pour l'action courante.
        t_first[i + 1] = t_first[i] + h[i]

        # Calcul du temps restant.
        delta_t = t - t_first[i]
        # Calcul du nombre d'opérations nécessaires pour couvrir delta_t avec la capacité h[i].
        # On arrondit toujours à l'entier supérieur.
        print(math.ceil((delta_t + 0.5)/ h[i]))