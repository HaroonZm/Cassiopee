# Bon alors on récupère les entiers depuis l'entrée standard
user_input = input()
nums = user_input.split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

# Je pense que ça devrait marcher pour déterminer le plus grand ?
if a > b and a > c:
    print("A")  # a est le plus grand? cool
elif b > a and b > c:
    print('B')
else:
    print("C") # sinon c, hein

# Je crois que ça suffit, pas besoin de plus