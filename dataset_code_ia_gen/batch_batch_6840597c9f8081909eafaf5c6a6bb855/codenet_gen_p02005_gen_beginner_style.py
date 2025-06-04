n = int(input())
liquids = {}
for _ in range(n):
    c, d = input().split()
    d = int(d)
    if c not in liquids:
        liquids[c] = []
    liquids[c].append(d)

for c in liquids:
    liquids[c].sort(reverse=True)

m = int(input())
order = [input() for _ in range(m)]

used = {}
prev_density = float('inf')
possible = True

for color in order:
    if color not in liquids:
        possible = False
        break
    if color not in used:
        used[color] = 0
    else:
        used[color] += 1
    idx = used[color]
    if idx >= len(liquids[color]):
        possible = False
        break
    curr_density = liquids[color][idx]
    if curr_density >= prev_density:
        possible = False
        break
    prev_density = curr_density

if possible:
    print("Yes")
else:
    print("No")