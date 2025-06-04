import sys
import heapq

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

V, E = map(int, input().split())
a = list(input().strip().split())

graph = [[] for _ in range(V)]
for _ in range(E):
    s, t = map(int, input().split())
    graph[s].append(t)
    graph[t].append(s)

# letters assigned to each node; None if not assigned yet
assigned = [None if x == '?' else x for x in a]

# For each node, store the set of letters used by neighbors
# But since degree <= 25, we can handle neighbors directly

# We will assign letters to nodes with initially '?' in order of their index,
# but only after taking care to assign the lex smallest letter not used by neighbor letters.
# As the problem states:
#  - While there is any '.' node unassigned:
#     - Select one unassigned node
#     - Assign smallest letter not used by neighbors
#  - Repeat until all assigned.

# To get lex smallest overall, assign in order of node index, each node when it becomes available:
# But problem says pick any unassigned node, so choosing in ascending index order is acceptable to get lex min.

# The problem states "そのような丸が存在しない場合はこの処理を終了する" - so keep assigning until no nodes remain unassigned

# To implement efficiently:
# We'll repeatedly try to assign letters to any unassigned node.
# But that can be costly to scan all nodes repeatedly.

# Optimization:
# Use a queue or priority queue of nodes that can be assigned now.
# Initially, nodes with '?' and at least one neighbor with assigned letter can't have all letters banned.
# So we must process nodes whose forbidden letters sets are less than 26.

# Initially, forbidden sets are calculated.

# However, neighbors may not be assigned, so forbidden sets may be empty.

# To model this, keep track for each node of letters assigned to neighbors
# Since some neighbors may also be unassigned, letters assigned only grow as we assign nodes.

# Because no node can have degree >= 26, for each node at least one letter is available.

# Approach:
# For each node with '?', we wait until assigned letters of neighbors are known.
# But since the process is sequential, after we assign a letter to a node,
# we update the forbidden letters of its neighbors.

# So we can use a queue of nodes ready to assign, i.e. nodes with '?' and where we can assign as forbidden letters known.

# Because the problem says to choose any unassigned node, to minimize lex order, pick the one with smallest index.

# So maintain a priority queue of such nodes.

# Initially, nodes with '?' are all candidates to assign.

# But assigning a letter before their neighbors' letters assigned may block some choices?

# Actually this problem is a typical greedy coloring problem,
# similar to graph coloring with 26 colors, with the twist that some nodes are pre-colored.

# The greedy approach is:
# For each uncolored node, assign the smallest letter not assigned to its neighbors.

# Since existing nodes with letters are fixed, and no node has degree >= 26, always possible.

# Implement greedy as:
# For i in [0..V-1]:
#    if assigned[i] is None:
#       forbidden = letters assigned to neighbors
#       assign smallest letter not in forbidden
#       assigned[i] = letter

# Because problem says "the process repeats while there exists any unassigned node".

# For performance, we do a single pass from 0 to V-1 assigning letters to unassigned nodes in order.

# This is justified because the problem wants lex smallest string overall,
# so assigning in ascending node order and assigning smallest possible letter each time is correct.

res = assigned[:]

for i in range(V):
    if res[i] is not None:
        continue
    forbidden = set()
    for nb in graph[i]:
        if res[nb] is not None:
            forbidden.add(res[nb])
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if c not in forbidden:
            res[i] = c
            break

print(''.join(res))