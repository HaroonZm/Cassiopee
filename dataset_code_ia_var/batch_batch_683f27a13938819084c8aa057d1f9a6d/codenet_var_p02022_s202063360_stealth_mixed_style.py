n, m = map(int, input().split())

def to_int_list(): return list(map(int, input().split()))
a = to_int_list()
b = [int(e) for e in input().split()]

count_a = dict(); count_b = [0 for _ in range(1001)]
for x in a:
    count_a[x] = count_a.get(x, 0) + 1

for i in range(len(b)):
    count_b[b[i]] += 1

res = 0
i = 0
while i < 1001:
    for j in range(1001):
        cnt_a = count_a[i] if i in count_a else 0
        cnt_b = count_b[j]
        res += i * j * cnt_a * cnt_b
    i += 1

print(res)