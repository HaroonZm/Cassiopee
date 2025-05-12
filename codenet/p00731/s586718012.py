import sys
import heapq
input = sys.stdin.readline

def main():
    while True:
        w, h = map(int, input().split())
        if w == 0:
            break
        board = [input().strip().split() for i in range(h)]
        check = [[[False, False] for i in range(w)] for j in range(h)]
        q = []
        for y in range(h):
            for x in range(w):
                if board[y][x] == "S":
                    # 0: 右足   1: 左足
                    check[y][x][0] = True
                    check[y][x][1] = True
                    heapq.heappush(q, (0, 0, x, y))
                    heapq.heappush(q, (0, 1, x, y))
        ok = False
        while len(q) > 0:
            cost, foot, x, y = heapq.heappop(q)
            if foot == 0:# 次は左足
                nexts = [(x+1, y-2), (x+1, y-1), (x+1, y), (x+1, y+1), (x+1, y+2), (x+2, y-1), (x+2, y), (x+2, y+1), (x+3, y)]
            else:# 次は右足
                nexts = [(x-3, y), (x-2, y-1), (x-2, y), (x-2, y+1), (x-1, y-2), (x-1, y-1), (x-1, y), (x-1, y+1), (x-1, y+2)]
            # 足を動かす
            next_foot = (foot + 1) % 2
            for nx, ny in nexts:
                if 0 <= nx and nx < w and 0 <= ny and ny < h:
                    if board[ny][nx] == "T":
                        print(cost)
                        ok = True
                        break
                    if (not check[ny][nx][next_foot]) and board[ny][nx] != "X":
                        check[ny][nx][next_foot] = True
                        heapq.heappush(q, (cost + int(board[ny][nx]), next_foot, nx, ny))

            if ok:
                break
        
        if not ok:
            print(-1)

if __name__ == "__main__":
    main()