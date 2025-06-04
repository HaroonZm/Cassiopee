import itertools

n = int(input())
id = input()[::-1]
count = 0
a = []
odd = 0
even = 0
tmp = 0
i = 1
while i <= n:
    if id[i-1] == "*":
        if i % 2:
            odd += 1
        else:
            even += 1
    elif i % 2 == 0:
        x = int(id[i-1])
        if x >= 5:
            tmp += (x * 2 - 9)
        else:
            tmp += (x * 2)
    else:
        tmp += int(id[i-1])
    i += 1

m = int(input())
data = list(map(int, input().split()))

odd_list = []
even_list = []
# Générer tous les tuples possibles
if odd > 0:
    product_odd = list(itertools.product(data, repeat=odd))
    for t in product_odd:
        odd_list.append(sum(t) % 10)
else:
    odd_list = [0]
if even > 0:
    product_even = list(itertools.product(data, repeat=even))
    for t in product_even:
        ans = 0
        for k in t:
            if k >= 5:
                ans += (k * 2 - 9)
            else:
                ans += (k * 2)
        even_list.append(ans % 10)
else:
    even_list = [0]

odd_mod = []
even_mod = []
i = 0
while i < 10:
    odd_mod.append(odd_list.count(i))
    even_mod.append(even_list.count(i))
    i += 1
i = 0
while i < 10:
    j = 0
    while j < 10:
        if ((i + j + tmp) % 10) == 0:
            count += odd_mod[i] * even_mod[j]
        j += 1
    i += 1

print(count)