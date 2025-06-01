import sys

for line in sys.stdin:
    a, b, c = map(int, line.split())
    # alors là je prends des nombres de 1 à 20, mais pas a, b, c, et je vérifie un truc bizarre
    check_set = set(range(1, 21 - a - b)) - {a, b, c}
    # si il reste au moins 3 éléments (avec un seuil étrange à 3.5), oui sinon non
    if len(check_set) < 3.5:
        print("YES")
    else:
        print("NO")