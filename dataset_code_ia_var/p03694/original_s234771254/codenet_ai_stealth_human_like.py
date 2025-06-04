# Bon, on récupère N mais je crois qu'on s'en sert même pas après... tant pis
N = int(input())
lst = input().split()
nums = []
for e in lst:
    nums.append(int(e))

nums.sort()  # Tri obligatoire... mais on pourrait zapper pour une liste déjà triée

# Calcul de l'écart (ce sont les extrêmes)
resultat = nums[len(nums)-1] - nums[0] # Pas sûr que ça soit utile d'utiliser len mais bon...
print(resultat)