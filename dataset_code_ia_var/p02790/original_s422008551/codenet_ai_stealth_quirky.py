import sys

def obfuscate(s, t):
    # Multiplie la chaîne s, t fois (t en entier)
    return s * int(t)

# utilise sys.stdin directement plutôt que input()
src = sys.stdin.readline
A, B = (lambda lst: (lst[0], lst[1]))(src().split())

# variables à un seul caractère majuscule
X = obfuscate(A, B)
Y = obfuscate(B, A)

# Expression booléenne dans un dictionnaire pour le choix de la sortie
{True: lambda: print(X), False: lambda: print(Y)}[X < Y]()