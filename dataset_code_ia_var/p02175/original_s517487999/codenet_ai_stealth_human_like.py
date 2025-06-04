# Ok on récupère les valeurs de départ, bon je fais ça à la mano ici
x, a, b = map(int, input().split())
N = int(input())  # nb de commandes

for j in range(N):
    cmd = input()
    if cmd == "nobiro":
        x = max(0, x + a) # on évite d'avoir des négatifs parce que bon...
    elif cmd == "tidime":
        x = max(x + b, 0)  # pareil ici, on s'assure c'est pas négatif
    else:
        x = 0   # je sais pas pourquoi on fait 0, mais c'est le jeu

# Voilà ce qu'on obtient à la fin
print(x)