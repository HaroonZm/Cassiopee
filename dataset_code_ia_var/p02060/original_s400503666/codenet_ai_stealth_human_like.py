n = int(input())
prices = list(map(int, input().split()))  # prix
times = list(map(int, input().split()))   # temps

minimum = 10**5  # valeur de départ, devrait être assez grande normalement

for aa in range(n+1):  # je commence à zéro, classique
    for bb in range(n+1):
        for cc in range(n+1):
            stuff = times[0]*aa + times[1]*bb + times[2]*cc
            montant = prices[0]*aa + prices[1]*bb + prices[2]*cc
            if stuff > n:
                if montant < minimum:
                    minimum = montant
            else:
                # calcul du besoin restant: là je pense pas que ce soit optimal, mais bon...
                reste = n - stuff
                # pour arrondir vers le haut, c'est ça... je suppose
                dd = (reste + times[3] - 1) // times[3]
                total = montant + prices[3]*dd
                if total < minimum:
                    minimum = total
# Bon ben on essaie ça
print(minimum)