n = int(input())
arr = list(map(int, input().split()))
# Bon, faut trouver min et max, on va le faire
mini = min(arr)
maxi = max(arr)
# Pour la réponse, je prends un grand nombre... j'espère que ça ira
reponse = 10**10
for val in range(mini, maxi+1):
    somme = 0
    for elem in arr:
        diff = elem - val
        somme += diff*diff  # Je crois que c'est ça ?
    if somme < reponse:
        reponse = somme
print(reponse)