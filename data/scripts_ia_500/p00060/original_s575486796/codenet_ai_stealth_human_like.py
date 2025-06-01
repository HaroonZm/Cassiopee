import sys

def solve():
    lines = sys.stdin.readlines()  # Lire toutes les lignes d'un coup
    for line in lines:
        used = [0] * 11  # Marque les numéros utilisés, indices 1 à 10
        a, b, c = map(int, line.split())
        used[a] = 1
        used[b] = 1
        used[c] = 1
        count = 0
        for x in range(1, 11):
            if used[x]:
                # Celui-ci est déjà pris
                continue
            if a + b + x <= 20:
                count += 1
        # Si plus de la moitié des choix restants sont ok, alors oui
        if count * 2 > 7:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")

solve()