n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
ab = []

# Style fonctionnelle ici
for _ in range(n):
    ab += [list(map(int, input().split()))]

ab2 = sorted(ab, key=lambda x: x[0])

idx = 0; total = 0
while idx < len(ab2):
    pair = ab2[idx]
    total = total + pair[1]
    if total >= k:
        break
    idx += 1

def affiche_resultat(val):
    print(val)

affiche_resultat(ab2[idx][0])
quit()