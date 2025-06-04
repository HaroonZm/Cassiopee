import sys
sys.setrecursionlimit(10**7)

class BDDNode:
    __slots__ = ('var', 'low', 'high')
    def __init__(self, var, low, high):
        self.var = var    # 0 or variable number (1-based)
        self.low = low    # for terminal: 0 or 1; for non-terminal: id of low child
        self.high = high  # for terminal: 0 or 1; for non-terminal: id of high child

def build_bdd(N, bit_line):
    """
    Recursively build BDD from truth table.
    Returns node id.
    Terminal nodes have var=0 and low/high being 0 or 1 terminal value.
    """
    # cache to memoize build calls
    memo = {}
    # unique table to keep unique nodes (reduce duplicates), maps (var, low, high) -> node id
    unique = {}

    # terminal nodes ids: 0 -> terminal 0, 1 -> terminal 1
    # We'll store terminals for convenience as node: var=0, low=val, high=val
    nodes = {0: BDDNode(0,0,0), 1: BDDNode(0,1,1)}

    def rec(level, start, length):
        # level: current variable index (1-based)
        # start: index in bit_line
        # length: section length (2^(N-level+1))
        if length == 1:
            # terminal node: leaf value is bit_line[start]
            val = 1 if bit_line[start] == '1' else 0
            return val
        if (level, start, length) in memo:
            return memo[(level,start,length)]
        half = length // 2
        low_id = rec(level+1, start, half)
        high_id = rec(level+1, start+half, half)

        # Reduction rule 1: if low == high, skip node
        if low_id == high_id:
            memo[(level,start,length)] = low_id
            return low_id
        key = (level, low_id, high_id)
        if key in unique:
            node_id = unique[key]
        else:
            node_id = len(nodes)
            nodes[node_id] = BDDNode(level, low_id, high_id)
            unique[key] = node_id
        memo[(level,start,length)] = node_id
        return node_id

    root = rec(1, 0, 2**N)
    return nodes, root

def count_variable_nodes(nodes):
    cnt = 0
    for node in nodes.values():
        if node.var != 0:
            cnt += 1
    return cnt

def main():
    input = sys.stdin.readline
    N = int(input())
    bit_line = input().strip()
    nodes, root = build_bdd(N, bit_line)
    print(count_variable_nodes(nodes))

if __name__ == "__main__":
    main()