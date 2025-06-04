import sys

sys.setrecursionlimit(10**7)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val  # operator or letter
        self.left = left
        self.right = right

def parse_hash(s, i=0):
    if s[i] in 'abcd':
        return Node(s[i]), i+1
    # else s[i] == '['
    op = s[i+1]
    left_node, ni = parse_hash(s, i+2)
    right_node, nj = parse_hash(s, ni)
    return Node(op, left_node, right_node), nj+1  # skip ']'

def eval_hash(node, P):
    # return value 0..15 as int
    if node.val in 'abcd':
        d = int(P['abcd'.index(node.val)])
        return d
    A = eval_hash(node.left, P)
    B = eval_hash(node.right, P)
    if node.val == '+':
        return A | B
    elif node.val == '*':
        return A & B
    else: # '^'
        return A ^ B

def count_eq(node, val):
    # return number of passwords (0..9999) whose hash == val for this node
    # Node is a tree of operations, val in 0..15
    # Letters correspond to digits 0..9 (0..15 total possible values, but only 0..9 used)
    # But letters only produce digit 0..9 (constraints)
    # We count possible 4-digit passwords which produce the final val.
    # We'll do it per node:
    # For letter: number of digits d in 0..9 with value d == val is 1 if val∈[0..9], else 0
    # For operator nodes:
    # val = f(a,b) with bitwise op, sum over all a,b in [0..15], count_left(a)*count_right(b) if f(a,b)==val
    # but letters produce only 0..9 so count(10..15)=0 in letter nodes
    # We'll do DP bottom up: at each node, create a dict val->count

    # We'll memoize:
    memo = {}

    def dfs(nd):
        if nd in memo:
            return memo[nd]
        if nd.val in 'abcd':
            dcount = [0]*16
            for d in range(10):
                dcount[d] = 1
            memo[nd] = dcount
            return dcount
        left_counts = dfs(nd.left)
        right_counts = dfs(nd.right)
        res = [0]*16
        for a in range(16):
            if left_counts[a] == 0:
                continue
            for b in range(16):
                if right_counts[b] == 0:
                    continue
                if nd.val == '+':
                    v = a | b
                elif nd.val == '*':
                    v = a & b
                else:
                    v = a ^ b
                res[v] += left_counts[a]*right_counts[b]
        memo[nd] = res
        return res

    all_counts = dfs(node)
    return all_counts[val]

def main():
    lines = sys.stdin.read().splitlines()
    i = 0
    while True:
        if i >= len(lines):
            break
        S = lines[i].strip()
        if S == '.':
            break
        P = lines[i+1].strip()
        i += 2
        root, _ = parse_hash(S, 0)
        val = eval_hash(root, P)
        cnt = count_eq(root, val)
        print(val, cnt)

main()