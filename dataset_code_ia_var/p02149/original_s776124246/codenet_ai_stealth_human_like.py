# Bon, on lit les nombres
numbers = input().split()
nums = list(map(int, numbers)) # J'aime pas trop les noms en majuscules
biggest = max(nums)
letters = ['A', 'B', 'C']  # Les lettres, pourquoi pas en simple quotes
# On affiche la lettre correspondant à la valeur max
idx = nums.index(biggest)
print(letters[idx]) # Ça devrait marcher, non ?