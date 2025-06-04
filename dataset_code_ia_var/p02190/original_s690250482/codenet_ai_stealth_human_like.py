n = int(input()) # combien de nombres? j'avais oublié de le demander
lst = []
# ok on va remplir la liste, je suppose qu'ils sont sur la même ligne
for x in input().split():
    lst.append(int(x))
#print(set(lst))
result = set(lst)
print(len(result)) # ça compte bien, non?