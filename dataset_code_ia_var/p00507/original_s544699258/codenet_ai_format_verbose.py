import itertools

# Demande à l'utilisateur combien de nombres il souhaite saisir
nombre_de_valeurs_a_saisir = int(input())

# Collecte les valeurs saisies par l'utilisateur et les stocke dans une liste
liste_des_nombres = [int(input()) for _ in range(nombre_de_valeurs_a_saisir)]

# Trie la liste pour prendre les plus petits éléments
liste_des_quatre_premiers_nombres_ordonnes = sorted(liste_des_nombres)[:4]

# Génére toutes les permutations possibles de 2 chiffres parmi les 4 nombres triés
liste_des_permutations_de_deux_chiffres = itertools.permutations(liste_des_quatre_premiers_nombres_ordonnes, 2)

# Concatène chaque paire pour former un nombre à deux chiffres
liste_des_nombres_a_deux_chiffres = [
    int(f'{premier_chiffre}{deuxieme_chiffre}')
    for premier_chiffre, deuxieme_chiffre in liste_des_permutations_de_deux_chiffres
]

# Trie la liste des nombres à deux chiffres générés
liste_des_nombres_a_deux_chiffres_ordonnes = sorted(liste_des_nombres_a_deux_chiffres)

# Affiche le troisième plus petit nombre à deux chiffres (index 2 car liste triée et indexée à 0)
print(liste_des_nombres_a_deux_chiffres_ordonnes[2])