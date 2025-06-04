n, m = map(int, input().split())
xy_list = []
for i in range(m):
    a, b = map(int, input().split())
    xy_list.append((a, b))

# Trie la liste par le premier élément du tuple
xy_list.sort()

min_y = [i for i in range(n)]
max_y = [i for i in range(n)]

for item in xy_list:
    index1 = item[1] - 1
    index2 = item[1]
    min_y[index2] = min_y[index1]
    max_y[index1] = max_y[index2]

ans = []
for i in range(n):
    ans.append(max_y[i] - min_y[i] + 1)

print(*ans)