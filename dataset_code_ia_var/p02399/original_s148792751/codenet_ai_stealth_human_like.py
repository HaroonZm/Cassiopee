# Bon alors on récupère les deux nombres
x, y = [int(v) for v in input().split()]
# Division entière
div = x // y
# Le reste, c'est utile parfois
modul = x % y
# La vraie division (attention à la précision !)
result = x / y

# J'affiche tout - attention au format, j'avoue ne jamais retenir la syntaxe
print(f"{div} {modul} {result:.5f}")