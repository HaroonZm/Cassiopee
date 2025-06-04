m = int(input())
n = int(input())
testimonies = []
for _ in range(n):
    x, y = map(int, input().split())
    testimonies.append((x, y))

# Tama is one suspect who can't testify but is seen entering last.
# Find Tama by noting that he is always after others.
# So, Tama must be the one who appears only on the right side of testimonies or not on left side.
# But problem states Tama is fixed to one suspect (not given in input), so we just know Tama does not testify.

# Build a graph of constraints: x must come before y
 # edges from x to y: x->y means x before y
graph = {i: [] for i in range(1, m+1)}
in_degrees = {i:0 for i in range(1, m+1)}

for x, y in testimonies:
    graph[x].append(y)
    in_degrees[y] += 1

# We know Tama is last, so the last one in order is Tama.
# Tama does not testify, so Tama does not appear as x in testimonies.
 # So find someone who never appears as x.
appears_as_x = set(x for x, y in testimonies)
tama_candidates = [i for i in range(1, m+1) if i not in appears_as_x]
# According to problem, Tama is exactly one person.
# Tama must be last, so put Tama last in order.
tama = tama_candidates[0]

# Topological sort to find one order that satisfies constraints
# To ensure Tama last, remove Tama from graph except for last step.

# Remove Tama from graph nodes to sort
nodes = [i for i in range(1, m+1) if i != tama]

# Build new in_degrees and graph without Tama
new_graph = {i: [] for i in nodes}
new_in_degrees = {i:0 for i in nodes}
for u in nodes:
    for v in graph[u]:
        if v != tama:
            new_graph[u].append(v)
            new_in_degrees[v] += 1

# Topological sort
order = []
queue = []
for node in nodes:
    if new_in_degrees[node] == 0:
        queue.append(node)

while queue:
    current = queue.pop(0)
    order.append(current)
    for nxt in new_graph[current]:
        new_in_degrees[nxt] -= 1
        if new_in_degrees[nxt] == 0:
            queue.append(nxt)

# Append Tama at last
order.append(tama)

for o in order:
    print(o)