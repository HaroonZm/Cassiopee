# Définition d'une fonction appelée 'ten_mod' qui prend un argument 'x'
def ten_mod(x):
    # Calcul du reste de la division de x par 10 pour obtenir le chiffre des unités de x
    # Si ce reste est égal à 0, alors on retourne 10, car x est déjà un multiple de 10 et il n'est pas nécessaire d'ajouter des unités pour atteindre le prochain multiple de 10
    # Sinon, on retourne le reste, c'est-à-dire le chiffre des unités de x
    ans = 10 if (x % 10) == 0 else x % 10
    # Retourne la valeur calculée à l'appelant
    return ans

# Lecture d'un nombre entier depuis l'entrée standard et conversion en entier avec la fonction int()
x = int(input())

# Calcul du premier élément de la variable 'ans' qui sera utilisée comme accumulation de la réponse finale
# Si x est divisible par 10 (c'est-à-dire un multiple de 10 : aucune unité restante après division par 10)
# alors ans prend la valeur de x directement car il est déjà un multiple de 10
# Sinon, on divise x par 10 (division entière avec int(x / 10)), puis on multiplie ce résultat par 10 
# pour obtenir la dizaine la plus proche inférieure, puis on ajoute 10 pour obtenir la dizaine supérieure suivante
ans = x if (x % 10) == 0 else int(x / 10) * 10 + 10

# Stocke la valeur initiale de x dans la variable 'last'
last = x

# Débute une boucle for qui itère 5-1 = 4 fois, car un élément a déjà été lu avant la boucle
for i in range(5 - 1):
    # À chaque itération, lit un nouvel entier entier depuis l'entrée standard et assigne à x
    x = int(input())
    # Pour chaque nouvel x, ajoute à 'ans' la même logique de multiple supérieur de 10:
    # si x est déjà un multiple de 10, on ajoute x directement 
    # sinon, on arrondit à la dizaine supérieure en prenant la dizaine inférieure et en ajoutant 10
    ans += x if (x % 10) == 0 else int(x / 10) * 10 + 10
    # Compare le résultat de ten_mod sur la variable 'last' et sur le nouvel x :
    # Si ten_mod(last) est strictement supérieur à ten_mod(x), alors cela signifie que 
    # le chiffre des unités de last est plus grand (ou vaut 10 si last finissait par 0)
    # Dans ce cas, on remplace last par x
    if ten_mod(last) > ten_mod(x):
        last = x

# Après la boucle, on ajuste la valeur finale de 'ans'
# Si le dernier 'last' n'est pas un multiple de 10 (c'est-à-dire (last % 10) != 0),
# alors on soustrait 10 et on ajoute le chiffre des unités de last à ans
# Sinon, on laisse ans inchangé
ans = ans - 10 + (last % 10) if (last % 10) != 0 else ans

# Affiche le résultat final à l'écran avec la fonction print()
print(ans)