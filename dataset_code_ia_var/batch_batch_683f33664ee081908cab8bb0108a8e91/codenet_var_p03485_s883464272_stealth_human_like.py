import math

# lecture des entrées... 
a, b = map(int, input().split())

# on essaie d'arrondir vers le haut, bon c'est ce que j'ai compris
resultat = math.ceil((a + b) / 2)

# affichage... peut-être pas nécessaire mais bon
print(resultat)