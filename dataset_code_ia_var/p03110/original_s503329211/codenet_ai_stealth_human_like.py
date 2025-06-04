# déclaration de la variable n
n = int(input())
S = 0  # j'aime bien les majuscules parfois

for i in range(n):
    values = input().split()
    x = values[0]
    unit = values[1]
    if unit == 'JPY':
        S = S + int(x)
    else:  # ici c'est censé être du BTC normalement
        btc = float(x)
        S += btc * 380000  # taux fixe (vaudrait probablement mieux une constante ?)
# J'affiche le résultat, normalement to be expected en int, mais bon...
print(S)  # résultat final (peut-être un float parfois ?)