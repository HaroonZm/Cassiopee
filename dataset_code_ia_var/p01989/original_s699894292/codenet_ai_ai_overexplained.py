import itertools  # Importe le module itertools, qui contient des outils pour manipuler des itérateurs, tel que 'combinations'

S = input()  # Demande à l'utilisateur de saisir une chaîne de caractères (généralement une suite de chiffres)
# À ce stade, S est une chaîne dont les caractères peuvent être accédés individuellement par leur index

ans = 0  # Initialise une variable compteur à 0, qui stockera le nombre de cas valides trouvés

# On veut examiner toutes les façons de diviser la chaîne S en 4 parties consécutives
# On doit choisir 3 indices (positions de coupe) dans la chaîne (à l'exclusion du tout début et de la fin)
# Les coupes possibles sont entre le caractère 1 (index 1) et le caractère de la longueur de S - 1 (index len(S)-1)

# itertools.combinations permet de générer toutes les combinaisons possibles de 3 indices issus de range(1, len(S))
# Chaque combinaison produite fournira les positions où faire les coupures pour former les 4 parties
for ptn in itertools.combinations(range(1, len(S)), 3):  # Pour chaque triplet d'indices de coupure possible (ordre croissant assuré)
    ai, bi, ci = ptn  # On extrait les trois indices de coupure de la combinaison courante

    # On effectue les découpages de la chaîne S aux indices trouvés
    a = S[:ai]      # 'a' correspond à la sous-chaîne de S qui va du début jusqu'à (exclu) ai
    b = S[ai:bi]    # 'b' va de ai (inclus) à bi (exclu)
    c = S[bi:ci]    # 'c' va de bi (inclus) à ci (exclu)
    d = S[ci:]      # 'd' va de ci (inclus) à la fin de la chaîne S

    # On veut vérifier si chacune de ces parties pourrait représenter un octet d'une adresse IPv4 (valeur entre 0 et 255)
    
    # Vérification n°1 : Un nombre écrit avec des zéros initiaux sauf pour le seul chiffre '0' n'est pas valide
    # Par exemple "01", "001" sont refusés alors que "0" tout seul est accepté
    if a[0] == '0' and a != '0':  # Si la sous-chaîne a commence par '0' mais n'est pas exactement '0'
        continue                 # On passe à la combinaison suivante (cette adresse serait invalide)
    if b[0] == '0' and b != '0':  # Même test pour la sous-chaîne b
        continue
    if c[0] == '0' and c != '0':  # Même test pour la sous-chaîne c
        continue
    if d[0] == '0' and d != '0':  # Même test pour la sous-chaîne d
        continue

    # Vérification n°2 : Chaque partie doit être un nombre dans l'intervalle [0,255] inclus
    # int(a) convertit la sous-chaîne 'a' en entier base 10
    if not 0 <= int(a) <= 255:  # Si la valeur n'est pas dans l'intervalle requis
        continue                # on passe à la prochaine combinaison
    if not 0 <= int(b) <= 255:  # De même pour la sous-chaîne b
        continue
    if not 0 <= int(c) <= 255:  # De même pour la sous-chaîne c
        continue
    if not 0 <= int(d) <= 255:  # De même pour la sous-chaîne d
        continue

    # Si toutes les conditions précédentes sont respectées, alors cette configuration forme une adresse valide
    ans += 1  # On incrémente notre compteur car on a trouvé une division valide de S en 4 parties correctes

print(ans)  # Affiche le nombre total de découpages valides trouvés pour la chaîne S