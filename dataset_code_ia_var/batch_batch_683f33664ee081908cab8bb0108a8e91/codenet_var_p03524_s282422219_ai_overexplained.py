# Demande à l'utilisateur de saisir une chaîne de caractères et l'assigne à la variable 's'
s = input()

# Calcule la longueur de la chaîne 's' à l'aide de la fonction len()
# Stocke le résultat dans la variable 'l'
l = len(s)

# Initialise à zéro un compteur pour la lettre 'a'
cnt1 = 0
# Initialise à zéro un compteur pour la lettre 'b'
cnt2 = 0
# Initialise à zéro un compteur pour la lettre 'c'
cnt3 = 0

# Démarre une boucle for pour parcourir chaque caractère de la chaîne 's'
# La boucle va de 0 jusqu'à l-1 inclus, ce qui permet de visiter chaque index valide de la chaîne
for i in range(l):
    # Vérifie si le caractère à la position 'i' de la chaîne est la lettre 'a'
    if s[i] == 'a':
        # Si c'est le cas, incrémente de 1 le compteur pour 'a'
        cnt1 += 1
    # Sinon, vérifie si le caractère est la lettre 'b'
    elif s[i] == 'b':
        # Si c'est le cas, incrémente de 1 le compteur pour 'b'
        cnt2 += 1
    # Sinon, vérifie si le caractère est la lettre 'c'
    elif s[i] == 'c':
        # Si c'est le cas, incrémente de 1 le compteur pour 'c'
        cnt3 += 1

# Après avoir compté les 'a', 'b', et 'c', réalise des vérifications logiques

# Utilise la fonction max() pour obtenir la plus grande valeur parmi les trois compteurs
# Vérifie si cette valeur maximale est exactement égale à 1
if max(cnt1, cnt2, cnt3) == 1:
    # Si c'est le cas, cela signifie qu'il y a au maximum une seule occurrence de chaque lettre
    # Affiche 'YES' (qui est une chaîne de caractères signifiant une validation positive)
    print('YES')
# Sinon, vérifie si l'un des compteurs est égal à zéro
elif cnt1 == 0 or cnt2 == 0 or cnt3 == 0:
    # Cela signifie qu'au moins une lettre (parmi 'a', 'b', ou 'c') est absente de la chaîne
    # Affiche 'NO' (réponse négative, car toutes les lettres ne sont pas présentes)
    print('NO')
# Sinon, vérifie le cas où la différence entre la valeur maximale et la valeur minimale des compteurs
# est inférieure ou égale à 1 (autrement dit, les trois compteurs sont proches les uns des autres)
elif max(cnt1, cnt2, cnt3) - min(cnt1, cnt2, cnt3) <= 1:
    # Si l'écart entre la valeur la plus grande et la plus petite ne dépasse pas 1
    # Cela signifie que les quantités de 'a', 'b' et 'c' sont presque égales
    # Affiche 'YES'
    print('YES')
# Si aucune des conditions précédentes n'est vraie (toutes les autres conditions ont échoué)
else:
    # Cela signifie que les différences sont trop importantes ou les conditions ne sont pas remplies
    # Affiche 'NO'
    print('NO')