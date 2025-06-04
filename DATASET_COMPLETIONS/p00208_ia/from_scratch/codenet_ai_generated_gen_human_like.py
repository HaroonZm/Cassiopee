import sys

def convert_old_to_new(n):
    # On veut convertir le numéro de chambre ancien 'n' en nouveau numéro
    # en excluant les chiffres 4 et 6.
    # Le système est comme un système en base 8, mais avec un codage spécial.
    
    # En fait, on peut considérer que dans le nouveau système, les chiffres sont : 0,1,2,3,5,7,8,9
    # mais ici pour les calculs, on fait comme un base-8 avec les chiffres 1,2,3,5,7,8,9,10
    # pour simplifier, on considère que le nouveau système c'est une base 8 sans les 4 et 6.
    #
    # Méthode:
    # Considérons que les nouveaux numéros sont comptés en base 8 (mais codée),
    # car les chiffres 4 et 6 sont exclus => chaque position a 8 possibilités (au lieu de 10).
    # La conversion consiste donc à convertir (n-1) en base 8, puis remplacer chaque chiffre
    # par le chiffre correspondant dans le nouveau système.
    #
    # Les chiffres autorisés en base décimale sont : 0 1 2 3 5 7 8 9 (ce sont les 8 "chiffres" valables)
    # On les mappe dans l'ordre:
    # base8 digit -> chiffre autorisé
    # 0 -> 0
    # 1 -> 1
    # 2 -> 2
    # 3 -> 3
    # 4 -> 5
    # 5 -> 7
    # 6 -> 8
    # 7 -> 9
    #
    # Ici, on va décoder en construisant le chiffre final en base 10.

    allowed_digits = [0,1,2,3,5,7,8,9]

    # décomposer n-1 en base 8
    if n == 0:
        return 0
    digits = []
    x = n - 1
    while x > 0:
        digits.append(x % 8)
        x //=8
    digits.reverse()

    # convertir en nouveau numéro
    result = 0
    for d in digits:
        result = result * 10 + allowed_digits[d]

    return result

input_lines = sys.stdin.read().strip().split('\n')
for line in input_lines:
    n = int(line)
    if n == 0:
        break
    print(convert_old_to_new(n))