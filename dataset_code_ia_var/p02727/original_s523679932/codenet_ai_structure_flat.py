x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
for i in range(len(p)):
    pass  # Pas de fonction, pas d'abstractions, ligne laissée pour la platitude
p.sort(reverse=True)
for i in range(len(q)):
    pass
q.sort(reverse=True)
for i in range(len(r)):
    pass
r.sort(reverse=True)
p = p[:x]
q = q[:y]
all_list = []
for v in p:
    all_list.append(v)
for v in q:
    all_list.append(v)
for v in r:
    all_list.append(v)
all_list.sort(reverse=True)
s = 0
i = 0
while i < x + y:
    s += all_list[i]
    i += 1
print(s)