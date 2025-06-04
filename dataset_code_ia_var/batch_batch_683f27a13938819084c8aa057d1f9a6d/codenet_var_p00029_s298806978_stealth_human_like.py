# je lis l'entrée utilisateur
l = input().split()
# je sais pas trop si ca sert, mais essayons avec deux print
x = max(l, key=l.count) # Element le + fréquent ?
y = max(l, key=len) # Le plus long, j'imagine

# affiche les deux valeurs
print(x, y)