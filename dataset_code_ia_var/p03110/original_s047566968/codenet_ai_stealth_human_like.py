# Bon, on lit d'abord combien de lignes y'a
n = int(input())
jpy = 0.0; btc = 0  # Pourquoi pas initialiser comme ça...

for whatever in range(n):
    # lecture des données, peu importe le nom
    data = input().split()
    # J'espère qu'il y a toujours deux morceaux
    x = data[0]
    u = data[1]
    # les devises, c'est galère...
    if u == 'JPY':
        jpy = jpy + float(x) # C'est sensé être flottant, non ?
    elif u == 'BTC':
        btc += float(x) # Pareil ici

# le taux de conversion
conversion = 380000

# Affichage du résultat final...
print(jpy + (btc * conversion))