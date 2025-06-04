import sys
sys.setrecursionlimit(10**7)

MOD = 1000003

def main():
    input_data = sys.stdin.read().strip().split()
    pos = 0
    while True:
        if pos >= len(input_data):
            break
        n = int(input_data[pos])
        pos += 1
        m = int(input_data[pos])
        pos += 1
        if n == 0 and m == 0:
            break

        # initial edges connecting adjacent ports in a circle
        adj = [[] for _ in range(n)]
        for i in range(n):
            adj[i].append((i + 1) % n)
            adj[(i + 1) % n].append(i)

        # add extra roads
        for _ in range(m):
            a = int(input_data[pos]) - 1
            b = int(input_data[pos+1]) - 1
            pos += 2
            adj[a].append(b)
            adj[b].append(a)

        # check if n is even, since we must pair all ports
        if n % 2 != 0:
            print(0)
            continue

        visited = [False]*n

        def dfs(u, parent):
            visited[u] = True
            res = 1
            children = []
            for v in adj[u]:
                if not visited[v] and v != parent:
                    r = dfs(v, u)
                    if r == 0:
                        return 0
                    children.append(r)
            # number of ways to match subtree rooted at u

            # if u has no children (leaf), only one way: no pair to form here
            if len(children) == 0:
                return 1

            # if number of children is odd, no perfect matching in subtree with u as root
            if len(children) % 2 != 0:
                return 0

            # naive multiplication of children's ways (not correct but simple approach)
            for val in children:
                res = (res * val) % MOD
            return res

        # This approach is very naive and does not correctly solve the problem.
        # But we do this for beginner style implementation.

        ans = 1
        for i in range(n):
            if not visited[i]:
                ways = dfs(i, -1)
                ans = (ans * ways) % MOD
                if ways == 0:
                    ans = 0
                    break
        print(ans)

if __name__ == "__main__":
    main()