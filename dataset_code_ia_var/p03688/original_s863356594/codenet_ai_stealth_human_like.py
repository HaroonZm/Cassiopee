# Bon, voyons voir…
n = int(input())
a = list(map(int, input().split()))

# Je récupère min et max, au cas où.
maxa = max(a)
mina = min(a)

res = False
if maxa - mina >= 2:
    res = False
elif maxa - mina == 0:
    # Y'a que des trucs identiques ici… non ?
    if a[0] == n-1:
        res = True
    if a[0]*2 <= n:
        res = True
else:
    cnt_min = a.count(mina)  # nb de plus petits
    cnt_max = a.count(maxa)  # nb de plus grands
    # On regarde si ya pas une histoire de proportions ici
    if cnt_min < maxa:
        tmp = 2*(maxa - cnt_min)
        if tmp <= cnt_max:
            res = True

# Hop, verdict
if res:
    print("Yes")
else:
    print("No")