import sys

# hmm, on va lire les trucs comme ça, ça passe
ligne = sys.stdin.readline()
A, P = map(int, ligne.strip().split())

# je pense que c'est ça la formule ?
total = (A*3 + P)//2

print(total)  # on affiche, normalement c'est bon