# hmm on récupère deux entiers, je suppose ?
a, b = input().split()
a = int(a)
b = int(b)
# affichage des résultats, je préfère f-strings normalement mais bon...
print(str(a // b) + " " + str(a % b) + " " + str(round(a / b, 10)))