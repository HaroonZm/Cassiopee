# Définition de la variable 'z' qui contient la chaîne de caractères de l'alphabet en minuscules.
# L'alphabet anglais comporte 26 lettres, de 'a' à 'z'.
z = 'abcdefghijklmnopqrstuvwxyz'

# Définition d'une fonction lambda 'e'.
# Une fonction lambda est une petite fonction anonyme en Python.
# Ici, 'e' prend trois paramètres : x (un caractère), i (un entier), et j (un entier).
# Elle retourne la lettre de l'alphabet correspondant à un certain décalage.
# z.index(x) donne la position de la lettre x dans l'alphabet (entre 0 et 25).
# On multiplie cet index par i, on ajoute j, puis on prend le modulo 26 pour rester dans l'alphabet.
# Le résultat est utilisé comme index pour accéder à la lettre correspondante dans 'z'.
e = lambda x, i, j: z[(z.index(x) * i + j) % 26]

# Définition d'une fonction nommée 'f' sans paramètres.
def f():
    # La fonction 'f' va essayer de trouver deux entiers i et j pour désencoder un texte chiffré.
    # Première boucle : i parcourt les entiers impairs de 1 à 25 (exclus 26), avec un pas de 2.
    for i in range(1, 26, 2):
        # Deuxième boucle : j parcourt tous les entiers de 0 à 25 (inclus), soit toutes les lettres de l'alphabet.
        for j in range(26):
            # La fonction va générer un mot chiffré à partir du mot 'that'
            # Elle utilise une compréhension pour appliquer la fonction 'e' à chaque lettre de 'that'
            mot1 = ''.join(e(c, i, j) for c in 'that')
            # Elle fait la même chose pour le mot 'this'
            mot2 = ''.join(e(c, i, j) for c in 'this')
            # La fonction vérifie si un de ces deux mots chiffrés est présent dans la chaîne s.
            # La chaîne 's' doit être accessible globalement.
            if mot1 in s or mot2 in s:
                # Si l'un des deux mots est trouvé, on retourne les valeurs de i et j, sous forme de tuple (i, j).
                return (i, j)

# Début de la boucle principale du programme
# Demande à l'utilisateur combien de fois il veut exécuter le programme ; 'input()' lit l'entrée utilisateur.
# int(input()) convertit l'entrée en entier. 
# [0]*n produit une liste de longueur n contenant des zéros, ce qui permet de réaliser n itérations en utilisant 'for'.
for _ in [0] * int(input()):
    # Lecture d'une ligne au clavier. On suppose que c'est la chaîne cryptée à décoder.
    s = input()
    # Calcul de l'alphabet décodé correspondant à la clé trouvée par 'f()'.
    # Pour chaque lettre c dans l'alphabet 'z', on applique la fonction 'e' avec les valeurs retournées par 'f()'.
    # Cela reconstitue l'alphabet d'origine servant à l'encodage du message.
    a = ''.join(e(c, *f()) for c in z)
    # Création d'une table de correspondance (mapping) pour la fonction translate().
    # str.maketrans(a, z) crée une table de traduction qui va remplacer chaque lettre de 'a' par la lettre correspondante dans 'z'.
    t = str.maketrans(a, z)
    # Affichage du texte décodé.
    # s.translate(t) applique la traduction à la chaîne s, remplaçant chaque lettre selon le mapping.
    print(s.translate(t))