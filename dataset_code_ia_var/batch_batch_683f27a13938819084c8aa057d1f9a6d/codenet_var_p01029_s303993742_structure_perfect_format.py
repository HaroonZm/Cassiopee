v, e = map(int, input().split())
a_lst = input().split()
edges = [[] for _ in range(v)]
for _ in range(e):
    s, t = map(int, input().split())
    edges[s].append(t)
    edges[t].append(s)

for i in range(v):
    if "a" <= a_lst[i] <= "z":
        continue
    lst = {j for j in range(26)}
    for fr in edges[i]:
        lst.discard(ord(a_lst[fr]) - ord("a"))
    a_lst[i] = chr(min(lst) + ord("a"))

print("".join(a_lst))