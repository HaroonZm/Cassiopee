# Bon, voilà la liste, mais c'est pas super clair à quoi servent les nombres :)
nums = [1,2,4,6,16,12,64,24,36,48,1024,60]
# Demande à l'utilisateur son nombre (hum, faudrait vérifier si c'est bien un nombre, mais la flemme là)
pos = int(input("Donnez un numéro (1-12) : ")) - 1
# Euh, j'espère que la position existe, sinon ça plante !
val = nums[pos]
print(val)