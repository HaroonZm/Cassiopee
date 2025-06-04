import sys
sys.setrecursionlimit(10**7)

def parse_blocks(s):
    blocks = []
    i = 0
    n = len(s)
    while i < n:
        acquired = []
        while i < n and s[i] != 'u':
            acquired.append(int(s[i]))
            i += 1
        i += 1  # skip 'u'
        blocks.append(acquired)
    return blocks

def build_wait_for_graph(blocks):
    m = len(blocks)
    g = [[] for _ in range(10)]
    # For each lock, find the set of blocks that acquire it
    lock_to_blocks = [[] for _ in range(10)]
    for i,b in enumerate(blocks):
        for l in b:
            lock_to_blocks[l].append(i)
    # Build dependency (wait-for) edges between locks
    # Check pairs of blocks that share locks to create wait edges between locks
    # If lock A is held by a thread in block i, and in block i another thread tries to acquire lock B which is held by block j,
    # then lock A waits for lock B, meaning edge from A to B
    for i in range(m):
        blocks_locks = set(blocks[i])
        # Each block holds all locks in blocks[i] simultaneously and releases all at u
        # The lock acquisition order in the block is linear, but since instructions are executed sequentially,
        # a thread holds the locks accumulated until the next u.
        # To simulate wait-for, for each lock in block i,
        # the thread tries to acquire locks in order in that block, so for subsequent locks in the block, 
        # the thread holds previous locks and tries to acquire next lock, generating edges.

    # Instead of modeling threads, we model a lock allocation graph:
    # For each block, locks are acquired in order, so within the block:
    # lock acquired later waits for locks held earlier in the block.
    # Outside the block, two blocks can cause waits if one tries to acquire a lock held by the other.
    # Because each thread acquires locks in sequence in the block until u.

    # Build edges within block: for locks acquired in order, later lock waits for earlier lock
    for b in blocks:
        for i in range(1,len(b)):
            g[b[i]].append(b[i-1])
    # Build edges between blocks: if two blocks share locks, cross edges possible
    # For each pair of locks (l1,l2), if l1 in block A and l2 in block B, and l2 is acquired later in block B, conflict may occur
    # But conflicts arise only if locks are used in different blocks and may cause circular waits.
    # We add edges from lock2 to lock1 if there exists blocks where lock1 is acquired before lock2.

    # To detect unsafe, we check if the graph (of locks) has cycles.

    return g

def dfs(u, g, visited, stack):
    visited[u] = 1
    for v in g[u]:
        if visited[v] == 0:
            if dfs(v, g, visited, stack):
                return True
        elif visited[v] == 1:
            return True
    visited[u] = 2
    stack.append(u)
    return False

def is_unsafe(s):
    blocks = parse_blocks(s)
    g = [[] for _ in range(10)]
    # Within each block, lock i+1 waits for lock i
    for b in blocks:
        for i in range(1,len(b)):
            g[b[i]].append(b[i-1])
    # Between blocks, if a lock l1 is acquired in a block after some other lock l2 is acquired in another block,
    # and lock l1 and l2 appear in different order in the sequence, this can generate waits.
    # But more generally, consider lock conflicts.
    # For each pair of locks (a,b), if there exists blocks containing a and b, where a waits for b indirectly, add edges accordingly.

    # Since all threads execute the same sequence from beginning,
    # cycles in lock dependency graph can happen if dependency graph formed by edges (latter lock waits for earlier lock) has cycle.

    visited = [0]*10
    for i in range(10):
        if visited[i]==0:
            if dfs(i, g, visited, []):
                return True
    return False

while True:
    n = sys.stdin.readline()
    if not n:
        break
    n = n.strip()
    if n == '0':
        break
    s = sys.stdin.readline().strip()
    if is_unsafe(s):
        print("UNSAFE")
    else:
        print("SAFE")