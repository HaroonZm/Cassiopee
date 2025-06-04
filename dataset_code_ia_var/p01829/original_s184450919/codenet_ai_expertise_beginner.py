import itertools
import sys

# Constantes utiles
INF = 10 ** 20

def S():
    return input()

def main():
    s = S()
    l = len(s)
    n = int(s)
    min_diff = INF
    result = ""
    max_val = 10 ** l

    for perm in itertools.permutations(range(10), l):
        # Éviter les zéros en tête
        if perm[0] == 0:
            continue
        numb = 0
        for digit in perm:
            numb = numb * 10 + digit
        diff = abs(n - numb)
        tmp = max(diff, max_val - diff)
        if tmp < min_diff:
            min_diff = tmp
            result = ""
            for digit in perm:
                result += str(digit)
    return result

print(main())