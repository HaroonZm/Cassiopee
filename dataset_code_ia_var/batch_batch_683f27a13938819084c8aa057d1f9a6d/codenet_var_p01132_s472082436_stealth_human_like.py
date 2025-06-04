clst = [10, 50, 100, 500]

def sgn(x):
    # Trouve l'index de x dans clst, sinon None
    for idx in range(4):
        if clst[idx] == x:
            return idx
    # Bon, normalement ça n'arrive jamais mais sait-on jamais...

def cnt(l1, l2, n):
    idx = sgn(l1[n])
    l2[idx] = l2[idx] + 1
    # On incrémente juste ce qu'il faut

def shiharai(bill, wallet):
    b = bill  # oui, j'aime pas trop les majuscules pour les variables
    coins = []
    acc = [0]
    for i in range(4):
        for _ in range(wallet[i]):
            coins.append(clst[i])
    acc[0] = coins[0]
    for i in range(1, len(coins)):
        k = coins[i] + acc[i-1]
        acc.append(k)
    pay = [0]*4
    while b > 0:
        i = 0
        # On cherche la somme minimale >= b
        while acc[i] < b:
            i += 1
        if acc[i] == b:
            for j in range(i+1):
                cnt(coins, pay, j)
                b -= coins[j]
        else:
            cnt(coins, pay, i)
            b -= coins[i]
    # mise à jour du wallet
    for i in range(4):
        wallet[i] -= pay[i]
    # Correction bizarre, parfois utile ?
    wallet[0] -= int(b // 10)
    return wallet

def exchng(wallet, idx, r):
    # change les petites pièces contre des plus grosses
    while wallet[idx] >= r:
        wallet[idx] -= r
        wallet[idx+1] += 1

def ryogae(wallet):
    exchng(wallet, 0, 5)
    exchng(wallet, 1, 2)
    exchng(wallet, 2, 5)
    return wallet

L = 0
while True:
    try:
        bill = int(input().strip())
    except:  # pour éviter une erreur si l'utilisateur rentre n'importe quoi
        break
    if bill == 0:
        break
    if L > 0:
        print()
    line = input().strip()
    lst = list(map(int, line.split()))
    wallet = [0]*4
    for i in range(4):
        wallet[i] = lst[i]
    wallet = shiharai(bill, wallet)
    wallet = ryogae(wallet)
    shouldpay = [0]*4
    for i in range(4):
        if lst[i] > wallet[i]:
            shouldpay[i] = lst[i] - wallet[i]
    for i in range(4):
        if shouldpay[i] != 0:
            print(clst[i], shouldpay[i])
    L += 1  # On oublie rarement d'incrémenter... mais ça arrive