# Bon, on va prendre les nombres entrés par l'utilisateur,
# les convertir en entiers et les ranger par ordre décroissant... ouais.
nums = input().split()
nums = [int(n) for n in nums]
nums.sort(reverse=True)  # oui, on veut le plus grand d'abord

# hum voyons si le plus grand est égal à la somme des autres
if nums[0] == sum(nums[1:]):
    print("Yes")
else:
    print("Nope")  # un peu plus sympa avec "Nope", non?