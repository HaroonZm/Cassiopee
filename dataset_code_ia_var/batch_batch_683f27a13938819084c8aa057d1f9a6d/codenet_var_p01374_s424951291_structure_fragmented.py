from collections import deque, defaultdict
import sys

def get_readline():
    return sys.stdin.readline

def get_write():
    return sys.stdout.write

def get_ca():
    return ord('a')

def aho_init():
    root = [None]*30
    root[-2] = 0
    root[-3] = 0
    root[-4] = 0
    nodes = [root]
    return root, nodes

def aho_get_code(c, ca):
    return ord(c) - ca

def aho_add_prepare():
    return []

def aho_add_child(node, nodes, code):
    child = [None]*30
    child[-2] = node[-2] + 1
    child[-3] = 0
    child[-4] = len(nodes)
    nodes.append(child)
    node[code] = child
    return child

def aho_add_single_char(node, c, ca, nodes):
    code = aho_get_code(c, ca)
    child = node[code]
    if not child:
        child = aho_add_child(node, nodes, code)
    return child

def aho_add_pattern(s, root, nodes, ca):
    node = root
    for c in s:
        node = aho_add_single_char(node, c, ca, nodes)
    node[-3] = 1

def aho_suffix_fill(v, root):
    if v[-1]:
        v[-3] += v[-1][-3]
    for i in range(26):
        if not v[i]:
            if v[-1]:
                v[i] = v[-1][i]
            else:
                v[i] = root[i] or root
            continue
        if v[-1]:
            v[i][-1] = v[-1][i]
        else:
            v[i][-1] = root

def aho_suffix_process_node(v, root, que):
    aho_suffix_fill(v, root)
    for i in range(26):
        if v[i]:
            que.append(v[i])

def aho_suffix_build(root):
    que = deque([root])
    while que:
        v = que.popleft()
        aho_suffix_process_node(v, root, que)
    root[-1] = root

class AhoCorasick:
    def __init__(self):
        self.root, self.nodes = aho_init()

    def add(self, s):
        aho_add_pattern(s, self.root, self.nodes, get_ca())

    def suffix(self):
        aho_suffix_build(self.root)

def read_ints(readline):
    return map(int, readline().split())

def initialize_graph_structs(N):
    mp = {}
    G = []
    S = []
    return mp, G, S

def node_encoding_func():
    ca = get_ca()
    return lambda x: ord(x) - ca

def add_word_to_map(f, mp, cur, G, S, fc):
    if f not in mp:
        mp[f] = cur
        G.append([])
        S.append(list(map(fc, f)))
        cur += 1
    return cur

def build_graph(N, readline, fc):
    mp, G, S = initialize_graph_structs(N)
    cur = 0
    for i in range(N):
        f, t = readline().strip().split()
        cur = add_word_to_map(f, mp, cur, G, S, fc)
        cur = add_word_to_map(t, mp, cur, G, S, fc)
        G[mp[f]].append(mp[t])
    return mp, G, S

def input_patterns(K, readline, tree):
    for i in range(K):
        s = readline().strip()
        tree.add(s)

def input_len_list(S):
    return list(map(len, S))

def build_G0(K, tree, L, S, M):
    G0 = [[None]*L for _ in range(K)]
    for k in range(K):
        nd0 = tree.nodes[k]
        g = G0[k]
        for i in range(L):
            s = S[i]
            if len(s) > M:
                continue
            nd = nd0
            c = 0
            for e in s:
                nd = nd[e]
                c += nd[-3]
            if c <= 1:
                g[i] = (nd[-4], c)
    return G0

def dp_init(M):
    return [defaultdict(int) for _ in range(M+1)]

def get_root_id(tree):
    return tree.root[-4]

def dp_first_fill(L, LS, G0, v0, dp):
    for i in range(L):
        e = G0[v0][i]
        if e is None:
            continue
        w, c = e
        dp[LS[i]][i, w, c] = 1

def dp_main_loop(M, dp, G, G0, LS, L, MOD):
    for i in range(M):
        for (v, p, c0), v0 in dp[i].items():
            v0 %= MOD
            g = G0[p]
            for w in G[v]:
                e = g[w]
                if e is None or i+LS[w] > M:
                    continue
                q, c = e
                if c0+c <= 1:
                    dp[i+LS[w]][w, q, c0+c] += v0

def dp_calc_answer(M, dp):
    ans = 0
    for (v, p, c0), v0 in dp[M].items():
        if c0 == 1:
            ans += v0
    return ans

def process_case(N, M, K, readline, write):
    if N == M == K == 0:
        return False
    fc = node_encoding_func()
    mp, G, S = build_graph(N, readline, fc)
    LS = input_len_list(S)
    tree = AhoCorasick()
    input_patterns(K, readline, tree)
    tree.suffix()
    L = len(S)
    K = len(tree.nodes)
    G0 = build_G0(K, tree, L, S, M)
    dp = dp_init(M)
    v0 = get_root_id(tree)
    dp_first_fill(L, LS, G0, v0, dp)
    dp_main_loop(M, dp, G, G0, LS, L, 10**9+7)
    ans = dp_calc_answer(M, dp)
    write("%d\n" % (ans % (10**9+7)))
    return True

def solve():
    readline = get_readline()
    write = get_write()
    while True:
        N, M, K = read_ints(readline)
        if not process_case(N, M, K, readline, write):
            break

solve()