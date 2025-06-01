from heapq import heappush, heappop
from sys import stdin

def main():
    h, w = map(int, stdin.readline().split())
    mp = [[-1]*(w+2)] + [[-1] + [int(c) if c.isdigit() else 0 if c == '.' else -1 for c in stdin.readline().strip()] + [-1] for _ in range(h)] + [[-1]*(w+2)]

    que = [(0, x, y) for y in range(1, h+1) for x in range(1, w+1) if mp[y][x] == 0]
    
    vec = ((0,1),(0,-1),(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1))
    heapify(que)
    
    turn = 0
    while que:
        turn, x, y = heappop(que)
        for dx, dy in vec:
            nx, ny = x + dx, y + dy
            if mp[ny][nx] > 0:
                mp[ny][nx] -= 1
                if mp[ny][nx] == 0:
                    heappush(que, (turn+1, nx, ny))
    print(turn)

if __name__ == "__main__":
    main()