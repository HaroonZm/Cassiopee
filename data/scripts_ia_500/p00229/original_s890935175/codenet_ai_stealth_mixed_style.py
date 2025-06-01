import os
import sys
import math
import bisect

def compute_score(b, r, g, c, s, t):
    # Utilisation d'une fonction classique avec calcul direct
    base = 100
    parts = [95*b, 63*r, 7*g, 2*c]
    penalty = 3 * (t - s)
    return base + sum(parts) - penalty

def main():
    if os.environ.get('PYDEV') == "True":
        sys.stdin = open("sample-input.txt", "r")

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        try:
            b, r, g, c, s, t = map(int, line.strip().split())
        except ValueError:
            continue
        if t == 0:
            break
        # utilisation d'une expression lambda pour calculer puis affichage direct
        score = (lambda b, r, g, c, s, t: 100 + 95*b + 63*r + 7*g + 2*c - 3*(t - s))(b, r, g, c, s, t)
        print(score)

# style impératif + direct, appel en global scope
if __name__ == "__main__":
    main()