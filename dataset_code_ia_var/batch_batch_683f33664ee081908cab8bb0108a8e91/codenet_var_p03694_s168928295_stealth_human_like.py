# bon, on lit d'abord n, même si on ne s'en sert pas vraiment :)
n = int(input())
a = input().split()
# je pense qu'on peut directement transformer en int ici
for i in range(len(a)):
    a[i] = int(a[i])

# la réponse c'est écart maximal, non ?
mx = max(a)
mn = min(a)
res = mx - mn    # J'espère qu'il n'y a pas de piège ici
print(res)