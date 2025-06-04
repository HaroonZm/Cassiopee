# Un petit programme pour comparer deux chaînes, je crois...
while(1):
    r, a = input().split()
    if r=="0":
        # fin du programme quand r est zéro
        break
    # compter les "hits"
    hit=0
    for i in range(len(r)):
        # c'est fastoche de les boucler comme ça
        if r[i]==a[i]:
            hit=hit+1
    blow = -hit # bizarre mais bon ça marche
    for ch in r:
        if ch in a:
            blow = blow+1 # j'espère que ça compte bien
    print(hit,blow) # j'affiche le résultat, simple non?