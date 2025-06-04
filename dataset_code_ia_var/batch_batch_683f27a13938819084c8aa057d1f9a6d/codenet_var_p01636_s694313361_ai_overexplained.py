# Demande une entrée à l'utilisateur sous forme de chaîne de caractères (même si c'est un nombre)
a = input()

# Initialise la variable 'ans' à 0, qui va compter le nombre de cas répondant aux critères
ans = 0

# Boucle for : parcourt les indices de 1 à la longueur de la chaîne 'a' moins 1, 
# car on veut toutes les coupures possibles du nombre sous forme de deux parties non vides.
for i in range(1, len(a)):
    # La variable 'df' contient la partie gauche de la coupure (sous forme de chaîne).
    # Cela correspond à tous les caractères de l'index 0 à i-1 inclus.
    df = a[:i]

    # La variable 'sm' contient la partie droite de la coupure (sous forme de chaîne).
    # Cela correspond à tous les caractères de l'index i jusqu'à la fin de la chaîne.
    sm = a[i:]

    # Vérifie si la première lettre de 'sm' est '0' (donc si 'sm' commence par un zéro),
    # car dans ce cas, convertir 'sm' en entier ne donnerait pas le résultat attendu
    # (ex: '012' deviendrait 12, ce qui n'est pas le comportement voulu pour un nombre découpé),
    # donc on ignore cette division du nombre en passant à la prochaine itération grâce au 'continue'.
    if sm[0] == "0":
        continue

    # Convertit la chaîne 'df' en un entier pour effectuer des opérations arithmétiques.
    df = int(df)

    # Convertit la chaîne 'sm' en un entier.
    sm = int(sm)

    # Vérifie trois conditions sur les entiers obtenus :
    # 1. (df + sm) % 2 == 0 : La somme des deux parties doit être paire.
    # 2. sm >= df : La partie droite doit être supérieure ou égale à la partie gauche.
    # 3. (sm - df) % 2 == 0 : La différence entre la partie droite et la partie gauche doit aussi être paire.
    if (df + sm) % 2 == 0 and sm >= df and (sm - df) % 2 == 0:
        # Si toutes les conditions sont réunies, on incrémente le compteur 'ans' de 1.
        ans += 1

# En dehors de la boucle : 
# On convertit la chaîne 'a' d'origine en entier et on vérifie si elle est paire (divisible par 2).
# Si c'est le cas, on ajoute 1 à 'ans', car le nombre lui-même satisfait une condition supplémentaire.
if int(a) % 2 == 0:
    ans += 1

# Affiche le résultat final à l'écran : le nombre total de cas respectant les critères donnés.
print(ans)