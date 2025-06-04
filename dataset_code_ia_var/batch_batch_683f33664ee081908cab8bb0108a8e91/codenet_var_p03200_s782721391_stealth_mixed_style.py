S = input()
N = len(S)
A = []
# Style procédural avec boucle for classique + comprehension
for idx in range(N):
    if S[idx] == "W":
        A += [idx]
# Style fonctionnel pour la gestion de n
n = (lambda x: len(x)-1)(A)
# Style impératif mais avec une fonction anonyme pour le calcul final
result = (lambda l, k: sum(l)-((k+1)*k//2))(A, n)
print(result)