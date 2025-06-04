import sys
sys.setrecursionlimit(10000)

def parse_tree(s):
    s = s.strip()
    if s[0] != '(':
        return int(s), None, None, s[len(str(int(s))):].lstrip()
    # parse '(' <left> ' ' <right> ')'
    assert s[0] == '('
    s = s[1:].lstrip()
    left, _, rest = parse_subtree(s)
    rest = rest.lstrip()
    right, _, rest2 = parse_subtree(rest)
    rest2 = rest2.lstrip()
    assert rest2[0] == ')'
    rest2 = rest2[1:]
    return None, left, right, rest2

def parse_subtree(s):
    s = s.lstrip()
    if s[0] == '(':
        node, left, right, rest = parse_tree(s)
        return (node, left, right), True, rest
    else:
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        num = int(s[:i])
        rest = s[i:]
        return (num, None, None), False, rest

def read_tree(line):
    line = line.strip()
    node, left, right, rest = parse_tree(line)
    return node, left, right

def evaluate_all_ways(node, left, right, leaves_sets, memo):
    # node, left, right represent the tree structure
    # leaves_sets is list of sets assigned to leaves by input
    # memo caches results for subtree (node, left, right)

    if node is not None:
        # leaf node: node is int index into leaves_sets (1-based)
        return [leaves_sets[node-1]]

    # internal node
    left_results = evaluate_all_ways(*left, leaves_sets, memo)
    right_results = evaluate_all_ways(*right, leaves_sets, memo)

    results = []
    for lset in left_results:
        for rset in right_results:
            # A: intersection
            a = lset & rset
            results.append(a)
            # O: union
            o = lset | rset
            results.append(o)
            # X: symmetric difference
            x = (lset | rset) - (lset & rset)
            results.append(x)

    return results

def count_ways(node, left, right, leaves_sets, memo):
    if node is not None:
        return {frozenset(leaves_sets[node-1]):1}

    key = (node, left, right)
    if key in memo:
        return memo[key]

    left_dp = count_ways(*left, leaves_sets, memo)
    right_dp = count_ways(*right, leaves_sets, memo)

    dp = {}
    for lset, lcount in left_dp.items():
        for rset, rcount in right_dp.items():
            # A: intersection
            a = lset & rset
            dp[a] = dp.get(a,0) + lcount*rcount
            # O: union
            o = lset | rset
            dp[o] = dp.get(o,0) + lcount*rcount
            # X: symmetric difference
            x = (lset | rset) - (lset & rset)
            dp[x] = dp.get(x,0) + lcount*rcount

    memo[key] = dp
    return dp

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line == "END":
            break
        # read tree
        node, left, right = read_tree(line)
        N = int(sys.stdin.readline())
        leaves_sets = []
        for _ in range(N):
            a,b,c,d = map(int, sys.stdin.readline().split())
            s = set()
            if a==1: s.add('a')
            if b==1: s.add('b')
            if c==1: s.add('c')
            if d==1: s.add('d')
            leaves_sets.append(s)

        memo = {}
        dp = count_ways(node, left, right, leaves_sets, memo)

        full_set = frozenset(['a','b','c','d'])
        print(dp.get(full_set, 0))

if __name__=="__main__":
    main()