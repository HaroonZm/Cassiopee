n, a, b = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)

# Calculer la factorielle simplement
def fact(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res

# Fonction de combinaison nCr
def comb(n, r):
    if r > n:
        return 0
    return fact(n) // (fact(r) * fact(n - r))

# Moyenne des 'a' premières valeurs
total = 0
for i in range(a):
    total += v[i]
average = total / a
print(average)

max_val = v[0]
min_val = v[a-1]

if max_val != min_val:
    cnt_min_in_selected = 0
    cnt_min_total = 0
    for i in range(a):
        if v[i] == min_val:
            cnt_min_in_selected += 1
    for num in v:
        if num == min_val:
            cnt_min_total += 1
    print(comb(cnt_min_total, cnt_min_in_selected))
else:
    count_min = 0
    for num in v:
        if num == min_val:
            count_min += 1
    ans = 0
    for i in range(a, b+1):
        if count_min >= i:
            ans += comb(count_min, i)
    print(ans)