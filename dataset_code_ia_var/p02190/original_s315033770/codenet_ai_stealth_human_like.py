# Bon, je récupère la taille (j'espère que c'est utile)
n = int(input())
s = set()  # un set, pratique pour l'unicité
lst = input().split()
nums = []
for elt in lst:
    nums.append(int(elt))  # Je fais comme ça, c'est plus clair pour moi

for idx in range(0, n):  # Je commence à zéro, comme d'hab
    s.add(nums[idx])

# ça donne le nombre d'éléments différents, normalement
print(len(s))