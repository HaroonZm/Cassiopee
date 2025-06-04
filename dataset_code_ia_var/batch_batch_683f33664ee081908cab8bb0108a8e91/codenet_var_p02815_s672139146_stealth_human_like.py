n = int(input())
clist = list(map(int, input().split()))
clist.sort(reverse=True) # Je préfère le tri ici
MOD = 1000000007

def power_fun(xx, nn):
    ans = 1
    while nn:
        if nn % 2:
            ans = ans * xx % MOD
        xx = (xx * xx) % MOD
        nn //= 2  # on divise
    return ans

s = 0
for idx in range(2, n+2):  # bizarre, enumerate commence à 2 ?
    try:
        s = (s + clist[idx-2] * idx) % MOD  # hum, je crois que ça marche...
    except: # il faudrait vérifier que la liste est assez longue
        break

# Un peu à la va-vite, je multiplie deux puissances comme dans l'autre code
resultat = s * power_fun(2, n-1)
resultat = (resultat * power_fun(2, n-1)) % MOD
print(resultat)