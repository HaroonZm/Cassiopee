from itertools import combinations  # Importe la fonction 'combinations' depuis le module 'itertools' pour générer des combinaisons possibles

S = raw_input()  # Lit l'entrée de l'utilisateur sous forme de chaîne de caractères et l'assigne à la variable S
N = len(S)  # Calcule la longueur totale de la chaîne S, c'est-à-dire le nombre de caractères, et l'assigne à N
cnt = 0  # Initialise le compteur de solutions valides à zéro

# On va essayer toutes les façons de placer trois séparateurs dans la chaîne, afin de pouvoir couper la chaîne S en 4 parties
# Les coupes se font entre les indices 1 et N-1 inclus pour a, b, c (on ne veut pas de chaînes vides)
# combinations(range(1, N), 3) va parcourir toutes les combinaisons possibles de trois indices distincts et triés croissants entre 1 et N-1 (exclusivement N)
for a, b, c in combinations(range(1, N), 3):
    ok = True  # On suppose au départ que la répartition actuelle est valide
    
    # Découpage de S suivant les séparateurs a, b, c:
    # A : depuis le début (indice 0) jusqu'à l'indice a (exclu)
    # B : depuis l'indice a jusqu'à l'indice b (exclu)
    # C : depuis l'indice b jusqu'à l'indice c (exclu)
    # D : depuis l'indice c jusqu'à la fin de la chaîne
    A = S[:a]
    B = S[a:b]
    C = S[b:c]
    D = S[c:]

    # On regroupe les 4 parties découpées dans une liste pour parcourir chacune d'elles
    for x in [A, B, C, D]:
        y = int(x)  # Convertit la sous-chaîne actuelle x en entier pour effectuer des vérifications numériques

        # Vérification 1 : l'entier doit être compris entre 0 et 255 inclus (comme pour une adresse IP standard)
        if y > 255:
            ok = False  # Si ce n'est pas le cas, on indique que la combinaison n'est pas valide

        # Vérification 2 : si la valeur entière y est zéro, alors la chaîne x doit être composé d'un unique caractère '0'.
        # Par exemple, '00', '000' ne sont pas valides, seul '0' l'est pour zéro.
        if y == 0 and len(x) != 1:
            ok = False

        # Vérification 3 : si la valeur entière n'est pas zéro, alors elle ne doit pas commencer par un zéro (pas de zéro initial comme dans '01' ou '007')
        if y != 0 and x[0] == '0':
            ok = False
    
    # Si toutes les conditions sont respectées (ok est toujours True), on incrémente le compteur de solutions valides
    cnt += ok

# Une fois toutes les combinaisons essayées, on affiche le nombre total de séparations valides trouvées
print cnt  # Affiche le résultat final à l'écran (nombre d'adresses IP valides générées depuis S)