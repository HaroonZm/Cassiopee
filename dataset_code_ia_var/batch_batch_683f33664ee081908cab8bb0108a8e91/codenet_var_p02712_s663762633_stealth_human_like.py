n = int(input())
answer = 0

# petit boucle pour compter
for val in range(1, n+1):
    # j'ignore les multiples de 3
    if val % 3 == 0:
        continue
    # aussi les multiples de 5, je crois
    if val % 5 == 0:
        continue
    # sinon j'ajoute
    answer = answer + val 

# ça affiche le résultat, normal
print(answer)