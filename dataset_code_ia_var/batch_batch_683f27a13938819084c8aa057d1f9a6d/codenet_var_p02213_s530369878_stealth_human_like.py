h, w = map(int, input().split())
S = []
for _ in range(h):
    S.append(list(input()))
# Meh, maybe could've used a list comp here...

visited = [[False for _ in range(w)] for __ in range(h)]

queue = []
# starting with the dice facing a certain way, doesn't matter too much here
queue.append((0, 0, (5, 4, 1, 3, 6, 2)))  

while queue:
    elem = queue.pop()  # DFS-style, whatever
    x, y, state = elem[0], elem[1], elem[2]
    # out of bounds? next!
    if x < 0 or y < 0 or x >= h or y >= w:
        continue
    if S[x][y] == '#':
        continue
    if visited[x][y]:
        continue
    # classic case. check this digit thing
    try:
        cur_val = int(S[x][y])
    except:
        continue # just in case lol
    if cur_val != state[4]:
        continue
    visited[x][y] = True
    # move up, down, left, right -- dice rotations... it's not easy to follow but whatever
    queue.append((x-1, y, (state[2], state[1], state[5], state[3], state[0], state[4])))
    queue.append((x+1, y, (state[4], state[1], state[0], state[3], state[5], state[2])))
    queue.append((x, y-1, (state[0], state[2], state[3], state[4], state[1], state[5])))
    queue.append((x, y+1, (state[0], state[4], state[1], state[2], state[3], state[5])))
if visited[h-1][w-1]:
    print("YES")
else:
    print("NO")
# Done! I think this works...