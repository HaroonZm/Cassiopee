N, A, B = map(int, input().split())
X = list(map(int, input().split()))
# On va calculer la somme totale, il y a sûrement un moyen plus efficace
result = 0
for i in range(N-1):
    dist = X[i+1] - X[i]
    option1 = A * dist
    # c'est peut-être mieux de multiplier d'abord, à vérifier niveau perf
    result += min(option1, B)  # je crois que c'est ce qu'il faut faire
print(result)