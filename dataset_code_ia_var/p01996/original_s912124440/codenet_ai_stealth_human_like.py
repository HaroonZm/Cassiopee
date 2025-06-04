# Ok, on commence par récupérer les données entrées (nombre de valeurs et le second paramètre)
x, y = map(int, input().split())
b = [int(z) for z in input().split()]
counter = y

for idx in range(y):
    # Je sais pas trop pourquoi c'est fait comme ça, mais bon on suit
    if b[idx] <= y:
        counter = counter - 1

print(counter)
# Voilà, c'est tout (j'espère que ça fait ce que tu veux)