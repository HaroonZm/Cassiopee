# Bon, on commence par récupérer le nombre de lignes :)
N = int(raw_input())  

otoshidama = []
for i in range(N):  # petite boucle "classique"
    parts = raw_input().split()
    otoshidama.append(parts)

ans = 0.0 # Alors ça, c'est le total, en yen en gros

for stuff in otoshidama:
    if stuff[1]=="JPY":
        ans += float(stuff[0]) 
    elif stuff[1] == 'BTC':
        ans += float(stuff[0]) * 380000  # le taux de conversion, faut pas l'oublier!
    # sinon on ignore, tant pis si y'a autre chose

# Je préfère ce print là, plus lisible, même si c'est python2... hum
print ans