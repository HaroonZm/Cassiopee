from collections import deque
db = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
dw = ((-1, 0), (0, -1), (1, 0), (0, 1))
def make():
    h, w = map(int, raw_input().split())
    if h == w == 0:
        return None
    P = ["."*(w+2)]+["."+raw_input()+"." for i in xrange(h)]+["."*(w+2)]
    deq = deque()
    w += 2; h += 2
    cnt = 0
    used = [[0]*w for i in xrange(h)]
    group = [None]
    for i in xrange(h):
        for j in xrange(w):
            if used[i][j]:
                continue
            cnt += 1
            c = P[i][j]
            dd = dw if c is '.' else db
            used[i][j] = cnt
            tmp = [(j, i)]
            deq.append((j, i))
            while deq:
                x, y = deq.popleft()
                for dx, dy in dd:
                    nx = x + dx; ny = y + dy
                    if 0 <= nx < w and 0 <= ny < h and not used[ny][nx] and P[ny][nx] == c:
                        used[ny][nx] = cnt
                        tmp.append((nx, ny))
                        deq.append((nx, ny))
            group.append(tmp)
    u = set()
    def dfs(num):
        result = []
        for x, y in group[num]:
            for dx, dy in dw:
                nx = x+dx; ny = y+dy
                if 0 <= nx < w and 0 <= ny < h and used[ny][nx] not in u:
                    v = used[ny][nx]
                    u.add(v)
                    result.append(dfs(v))
        return sorted(result)
    return dfs(1)
while 1:
    A = make()
    if not A:
        break
    B = make()
    if A == B:
        print "yes"
    else:
        print "no"