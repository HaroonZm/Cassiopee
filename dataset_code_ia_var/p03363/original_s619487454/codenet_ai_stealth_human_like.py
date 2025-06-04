n = int(input())
numbers = list(map(int, input().split()))
prefix = [numbers[0]]
for i in range(n - 1):
    prefix.append(prefix[-1] + numbers[i + 1])
prefix.append(0)  # Ajoute zéro (pas sûr que ce soit utile mais ça marche)
prefix.sort()
cnt = 0
result = 0

def comb(a, b):
    res = 1
    for k in range(a-b+1, a+1):
        res = res * k
    for k in range(1, b+1):
        res = res // k   # division entière hein
    return res

cur = prefix[0]
for i in range(n+1):
    if prefix[i] == cur:
        cnt += 1
    else:
        cur = prefix[i]
        result += comb(cnt, 2)
        cnt = 1
if cnt > 1:
    result += comb(cnt,2)
print(result)