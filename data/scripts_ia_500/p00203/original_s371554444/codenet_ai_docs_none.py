import sys
from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

def solve(field):
    BLANK, OBSTACLE, JUMP = 0, 1, 2
    ans = 0
    dx = [0, -1, 1]
    x_limit = len(field[0])
    y_limit = len(field)
    path = defaultdict(int)
    Q = deque()
    for x, m in enumerate(field[0]):
        if m == BLANK:
            k = '{}_{}'.format(x, 0)
            Q.append((x, 0))
            path[k] = 1
    while Q:
        cx, cy = Q.popleft()
        k = '{}_{}'.format(cx, cy)
        num = path.pop(k)
        if field[cy][cx] == OBSTACLE:
            continue
        elif field[cy][cx] == JUMP:
            if cy+2 > y_limit-1:
                ans += num
            else:
                k = '{}_{}'.format(cx, cy+2)
                if not path[k]:
                    Q.append((cx, cy+2))
                path[k] += num
            continue
        elif cy == y_limit -1:
            ans += num
            continue
        for i in range(3):
            nx = cx + dx[i]
            ny = cy + 1
            if 0<= nx < x_limit:
                if field[ny][nx] == JUMP and dx[i] == 0:
                    if ny+2 > y_limit - 1:
                        ans += num
                    else:
                        k = '{}_{}'.format(nx, ny+2)
                        if not path[k]:
                            Q.append((nx, ny+2))
                        path[k] += num
                elif field[ny][nx] == BLANK:
                    if (ny >= y_limit - 1):
                        ans += num
                    else:
                        k = '{}_{}'.format(nx, ny)
                        if not path[k]:
                            Q.append((nx, ny))
                        path[k] += num
    return ans

def main(args):
    while True:
        X, Y = map(int, input().strip().split())
        if X == 0 and Y == 0:
            break
        field = []
        for _ in range(Y):
            temp = [int(x) for x in input().strip().split()]
            field.append(temp)
        result = solve(field)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])