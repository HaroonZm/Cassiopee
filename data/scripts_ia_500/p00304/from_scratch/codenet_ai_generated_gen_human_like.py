import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

N = int(sys.stdin.readline())
nodes = [None]*(N+1)
for i in range(1, N+1):
    s = sys.stdin.readline().strip()
    if s.endswith('?'):
        option = True
        s = s[:-1]
    else:
        option = False
    if s == 'E':
        nodes[i] = ('E', option, [])
    else:
        # s is 'A' or 'R'
        nodes[i] = (s, option, [])

children = [[] for _ in range(N+1)]
parent = [0]*(N+1)
for _ in range(N-1):
    s, t = map(int, sys.stdin.readline().split())
    children[s].append(t)
    parent[t] = s

for i in range(1, N+1):
    tp, opt, _ = nodes[i]
    nodes[i] = (tp, opt, children[i])

def dfs(u):
    tp, opt, ch = nodes[u]
    if tp == 'E':
        # E node
        if opt:
            # option: 2 choices: pick or not pick
            # if pick: must pick and then children (none)
            # if not pick: 1 way(no children to pick)
            # no children for E node
            return 2
        else:
            # not optional E node: must pick
            return 1
    else:
        # A or R node
        # children are not optional E nodes
        vals = [dfs(c) for c in ch]
        if tp == 'A':
            # alt node: must pick exactly one child if not optional, or zero or one child if optional
            total = 0
            for v in vals:
                total += v
            total %= MOD
            if opt:
                # can pick none or one
                total = (total + 1) % MOD
            return total
        else:
            # R node (or type)
            # if not optional: must pick at least one child
            # if optional: pick zero or more children (at least 0)
            mul_all_plus1 = 1
            for v in vals:
                mul_all_plus1 = (mul_all_plus1 * (v + 1)) % MOD
            if opt:
                # zero or more children, including zero
                return mul_all_plus1 % MOD
            else:
                # at least one child
                return (mul_all_plus1 - 1) % MOD

print(dfs(1)%MOD)