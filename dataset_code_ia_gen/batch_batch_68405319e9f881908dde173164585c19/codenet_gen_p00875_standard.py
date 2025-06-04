from collections import deque

def apply_substitution(s, alpha, beta):
    res = []
    i = 0
    n = len(s)
    la = len(alpha)
    while i <= n - la:
        if s[i:i+la] == alpha:
            res.append(beta)
            i += la
        else:
            res.append(s[i])
            i += 1
    res.append(s[i:])
    return ''.join(res)

def solve():
    while True:
        n = input().strip()
        if n == '0':
            break
        n = int(n)
        subs = []
        for _ in range(n):
            a,b = input().split()
            subs.append((a,b))
        gamma = input()
        delta = input()
        from collections import deque
        visited = set()
        queue = deque()
        queue.append((gamma,0))
        visited.add(gamma)
        ans = -1
        while queue:
            curr, steps = queue.popleft()
            if curr == delta:
                ans = steps
                break
            if steps >= 20: # Limit depth to avoid infinite loops
                continue
            for a,b in subs:
                # If alpha not in curr, no substitution possible
                if a not in curr:
                    continue
                new_s = apply_substitution(curr,a,b)
                if new_s not in visited and len(new_s) <= 10*21:
                    visited.add(new_s)
                    queue.append((new_s, steps+1))
        print(ans)

if __name__ == "__main__":
    solve()