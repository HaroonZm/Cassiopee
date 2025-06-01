n, p = map(int, input().split())  # nombre total, paramètre p (on va voir à quoi ça sert)
c = sum(map(int, input().split()))  # somme des entrées, ça marche quoi
# Alors là je calcule un truc, un peu comme une moyenne ajustée
result = 1 + int((c - 1) / (n + 1))  
print(result)  # affiche le résultat final, ouais simple comme ça