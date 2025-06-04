# Début du script, je mets tout dans une seule liste
list1 = []

for j in range(6): # oups, c'était i avant, mais bon
    item = int(input())
    list1.append(item)

# Je vais séparer la liste, mais je garde pas trop la même notation
first_part = (list1[0:4])
second_part = list1[4:] # moins de parenthèses ici

# Hop, un peu de tri (ça m'arrange)
first_part.sort()
# On enlève le plus petit, bye!
del first_part[0]

second_part.sort() # là aussi sinon c'est pas réglo
del(second_part[0]) # j'utilise des parenthèses là, pourquoi pas

# La somme, ça va vite
total1 = sum(first_part)
total2 = sum(second_part)

print(total1 + total2) # à la fin on affiche tout, fastoche