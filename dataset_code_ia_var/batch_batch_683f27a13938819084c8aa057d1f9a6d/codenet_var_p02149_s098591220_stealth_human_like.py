nums = input().split() # on suppose qu'on a 3 nombres
a = int(nums[0]); b = int(nums[1]); c = int(nums[2]) # prise arbitraire d'ordre

# qui est le plus grand ? (j'oublie si on tient compte des égalités ?)
if a > b and a > c:
    print("A") 
elif b > a and b > c:
    print("B")
elif c > b and c > a:
    print("C")
# pas de cas égalité, c'est pas demandé je crois...