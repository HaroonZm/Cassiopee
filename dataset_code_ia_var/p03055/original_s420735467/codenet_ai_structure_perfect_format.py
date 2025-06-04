import queue

n = int(input())
tree = {i: [] for i in range(n)}

for _ in range(n - 1):
    t = input().split()
    u, v = int(t[0]), int(t[1])
    tree[u - 1].append(v - 1)
    tree[v - 1].append(u - 1)

a = 0
q = queue.Queue()
q.put(a)
v = [0 for _ in range(n)]
v[a] = 1

while not q.empty():
    a = q.get()
    for b in tree[a]:
        if v[b] == 0 and len(tree[b]) > 1:
            q.put(b)
            v[b] = 1

s = a
q = queue.Queue()
q.put([a, 1])
v = [0 for _ in range(n)]
v[a] = 1

while not q.empty():
    a = q.get()
    for b in tree[a[0]]:
        if v[b] == 0 and len(tree[b]) > 1:
            q.put([b, a[1] + 1])
            v[b] = 1

if n <= 3:
    l = n
else:
    l = a[1] + 2

if l % 3 == 2:
    print("Second")
else:
    print("First")