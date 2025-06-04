n = int(input())
names = []
prices = []
name_to_index = {}

for i in range(n):
    data = input().split()
    names.append(data[0])
    prices.append(int(data[1]))
    name_to_index[data[0]] = i

parent = []
for i in range(n):
    parent.append(i)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

m = int(input())
for j in range(m):
    s, t = input().split()
    i1 = name_to_index[s]
    i2 = name_to_index[t]
    p1 = find(i1)
    p2 = find(i2)
    parent[p1] = p2

group_min_price = {}
group_count = {}

for i in range(n):
    root = find(i)
    if root in group_min_price:
        if prices[i] < group_min_price[root]:
            group_min_price[root] = prices[i]
        group_count[root] += 1
    else:
        group_min_price[root] = prices[i]
        group_count[root] = 1

result = 0
for root in group_min_price:
    result += group_min_price[root] * group_count[root]
print(result)