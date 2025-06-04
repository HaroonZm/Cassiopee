import numpy as np  # Importe la bibliothèque numpy qui fournit des outils puissants pour manipuler des tableaux numériques

# Crée un tableau numpy de taille 26 rempli de zéros. Chaque case correspond à une lettre majuscule de l'alphabet anglais (A-Z).
C_vec = np.zeros(26)

# Demande à l'utilisateur de saisir deux nombres entiers séparés par un espace, puis les récupère en tant qu'entiers.
# 'N' représente probablement le nombre total d'éléments à traiter, 'K' un facteur utilisé plus loin dans le code.
N, K = map(int, raw_input().split())

# Boucle sur une plage allant de 0 à N-1 (soit N itérations au total). À chaque itération :
for i in range(N):
    # Demande à l'utilisateur de saisir une chaîne de caractères (probablement une lettre).
    # Prend le premier caractère de la chaîne saisie (grâce à l'indice [0]).
    # Convertit ce caractère en sa valeur entière unicode avec 'ord()'.
    # Soustrait à cette valeur celle de 'A' afin de ramener l'intervalle entre 0 et 25 (A=0, B=1, ..., Z=25).
    # Incrémente la case correspondante du tableau C_vec de 1, ce qui permet de compter combien de fois chaque lettre apparaît.
    C_vec[ord((raw_input()[0])) - ord('A')] += 1

# Démarre une boucle infinie qui ne se terminera que lorsqu'on rencontrera une instruction 'break'.
while True:
    # Calcule la somme de toutes les valeurs du tableau C_vec (donc, le total des comptages des lettres).
    # Divise cette somme par K puis convertit le résultat en entier, ce qui donne la valeur maximale autorisée 'm'.
    m = int(C_vec.sum() / K)

    # Applique la fonction 'np.minimum' entre tout le tableau C_vec et la valeur m.
    # Cela tronque chaque élément de C_vec à m (tout élément supérieur devient m).
    C_vec = np.minimum(C_vec, m)

    # Calcule une nouvelle valeur 'm_next' en refaisant le calcul de la moyenne entière mis à jour après tronquage.
    m_next = int(C_vec.sum() / K)

    # Si la nouvelle valeur 'm_next' est identique à la précédente 'm', cela signifie que la distribution a convergé.
    if m_next == m:
        # Sort de la boucle infinie car la condition d'arrêt est atteinte.
        break
    else:
        # Si la condition n'est pas atteinte, on recommence une itération avec éventuellement une nouvelle valeur m.
        m = m_next

# Affiche la valeur finale de m sur la sortie standard (en général l'écran).
print m