import sys
sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline
    while True:
        n,a,s,g = map(int,input().split())
        if n==0 and a==0 and s==0 and g==0:
            break
        graph = [[] for _ in range(n)]
        for _ in range(a):
            x,y,lab = input().split()
            x=int(x)
            y=int(y)
            graph[x].append((lab,y))
        # Sort edges to visit lex smaller labels first for deterministic order
        for edges in graph:
            edges.sort(key=lambda e:e[0])
        dp = [None]*n
        visiting = [False]*n

        def dfs(u):
            if dp[u] is not None:
                return dp[u]
            if visiting[u]:
                # Detect cycle on path -> infinite possibility -> no smallest
                dp[u] = None
                return None
            visiting[u]=True
            if u == g:
                dp[u] = ""
                visiting[u]=False
                return dp[u]
            candidates = []
            for lab,v in graph[u]:
                suffix = dfs(v)
                if suffix is not None:
                    candidates.append(lab+suffix)
            visiting[u]=False
            if not candidates:
                dp[u] = None
            else:
                dp[u] = min(candidates)
            return dp[u]

        ans = dfs(s)
        if ans is None:
            print("NO")
        else:
            # Check for infinite improvement by cycles:
            # if there exists a cycle on reachable path from s to g,
            # which can prepend 'a' to any spell to get lex smaller,
            # then answer is NO.
            # Actually above dp with cycle detection returns None for cycles,
            # so no infinite better spell possible.
            print(ans)

if __name__ == "__main__":
    main()