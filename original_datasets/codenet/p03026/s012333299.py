from collections import deque

N = int(input())
to = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(lambda x:int(x) - 1, input().split())
    to[a].append(b)
    to[b].append(a)

c = list(map(int, input().split()))
c.sort()

def main():
    ans = [0] * N
    ans[0] = c.pop()
    S = 0

    seen = [0] * N
    seen[0] = 1
    que = deque([0])

    while que:
        v = que.popleft()
        for nv in to[v]:
            if not seen[nv]:
                seen[nv] = 1
                ans[nv] = c.pop()
                S += ans[nv]
                que.append(nv)

    print(S)
    print(*ans)

if __name__ == "__main__":
    main()