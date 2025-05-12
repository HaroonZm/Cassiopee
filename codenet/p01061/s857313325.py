n, m = map(int, input().split())
parent = [i for i in range(n)]

def get_par(x):
    if x == parent[x]:return x
    parent[x] = get_par(parent[x])
    return parent[x]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    pa, pb = get_par(a), get_par(b)
    parent[pb] = pa

city_dic = set()
village_cnt = 0
for i in range(n):
    pi = get_par(i)
    if i == pi:village_cnt += 1
    else:city_dic.add(pi)

print(abs(2 * len(city_dic) - village_cnt))