from collections import deque

def main():
    h, w, n = map(int, input().split())
    mp = [list("#" * (w + 2))] + [list("#" + input() + "#") for _ in range(h)] + [list("#") * (w + 2)]
    init_body = [None] * 4
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if mp[y][x] == "S":
                init_head = (x, y)
                mp[y][x] = "."
            if mp[y][x] == "e":
                mp[y][x] = "."
            if "a" <= mp[y][x] <= "d":
                init_body[ord(mp[y][x]) - ord("a")] = (x, y)
                mp[y][x] = "."
            if "1" <= mp[y][x] <= "9":
                mp[y][x] = int(mp[y][x])
    
    que = deque()
    que.append((0, init_head, init_body, 1))
    mem = {}
    mem[(init_head, tuple(init_body), 1)] = 0
    vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
    while que:
        score, head, body, target = que.popleft()
        if target > n:
            print(score)
            break
        x, y = head
        for dx, dy in vec:
            nx, ny = x + dx, y + dy
            if (nx, ny) in body:continue
            if mp[ny][nx] == "#":continue
            new_target = target
            if mp[ny][nx] == target:new_target += 1
            new_body = tuple([head] + list(body)[:-1])
            if ((nx, ny), new_body, new_target) not in mem:
                mem[((nx, ny), new_body, new_target)] = True
                que.append((score + 1, (nx, ny), new_body, new_target))
    else:
        print(-1)

main()