def plus(s):
    """
    Met à jour le tableau global 'c' en tenant compte du caractère actuel 's' et des états définis dans 'g'.
    Pour chaque état possible, on accumule dans 'd' le nombre de façons d'atteindre cet état en se basant sur
    les intersections d'états avec 's', puis on remplace 'c' par 'd'.

    Args:
        s (str): Lettre courante à traiter parmi 'J', 'O', ou 'I'.
    """
    global c
    # Liste temporaire pour compter les combinaisons pour chaque état
    d = [0] * 7
    for i in range(7):
        # Si la lettre courante 's' est présente dans le sous-ensemble représenté par g[i]
        if s in g[i]:
            for j in range(7):
                # Si l'intersection entre deux états n'est pas vide, il y a continuité possible
                if g[i] & g[j] != set():
                    d[i] += c[j]
    # Mise à jour du compteur global avec les nouvelles valeurs calculées
    c = d

# Lecture du nombre de caractères de la séquence à traiter
n = int(input())
# Lecture de la séquence elle-même (chaîne de caractères sur l'alphabet 'J', 'O', 'I')
s = input()

# Définition de tous les sous-ensembles possibles de {'J','O','I'}, en ignorant l'ensemble vide
g = [set(["J"]), set(["O"]), set(["I"]), set(["J", "O"]), set(["J", "I"]), set(["O", "I"]), set(["J", "O", "I"])]

# Initialisation du tableau des comptages pour chaque état possible.
# c[i] est le nombre de façons d'obtenir l'état g[i] après lecture d'une certaine position de la séquence
# Le dernier élément supplémentaire sert à initialiser c[0] = 1 (au départ on commence sans rien avoir choisi)
c = [1, 0, 0, 0, 0, 0, 0, 0]

# Boucle principale : on traite chaque caractère de la séquence l'un après l'autre
for i in range(n):
    plus(s[i])

# On affiche la somme des différentes façons de remplir la contrainte modulo 10007
print(sum(c) % 10007)