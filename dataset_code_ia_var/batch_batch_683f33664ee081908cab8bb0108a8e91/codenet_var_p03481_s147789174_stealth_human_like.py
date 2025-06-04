# Bon, on récupère deux nombres
input_line = input()
a, s = map(int, input_line.strip().split())
result = 0
# On va boucler tant que a est plus petit que s
while a <= s:
    result = result + 1  # incremente, classique
    a = a * 2  # multiplie (ça va vite)
# On affiche le résultat
print(result)
# c'est pas super joli mais bon, ça marche