import sys
from collections import deque

def get_input():
    return sys.stdin.readline().strip()

def map_ints():
    return map(int, get_input().split())

def list_map_ints():
    return list(map(int, get_input().split()))

def initialize_tree(n):
    return [[] for _ in range(n + 1)]

def read_edges(tree, n):
    for _ in range(n - 1):
        add_edge(tree)

def add_edge(tree):
    a, b, c = map_ints()
    tree[a].append([a, b, c])
    tree[b].append([b, a, c])

def initialize_ans(n):
    ans = [-1] * (n + 1)
    ans[1] = 0
    return ans

def initialize_queue(tree):
    que = deque()
    que.append(tree[1])
    return que

def process_queue(que, tree, ans):
    while queue_not_empty(que):
        process_node(que, tree, ans)

def queue_not_empty(que):
    return len(que) > 0

def process_node(que, tree, ans):
    q = que.popleft()
    process_edges(q, que, tree, ans)

def process_edges(q, que, tree, ans):
    for x, y, z in q:
        process_edge(x, y, z, que, tree, ans)

def process_edge(x, y, z, que, tree, ans):
    if ans[y] == -1:
        ans[y] = (ans[x] + z) % 2
        que.append(tree[y])

def print_answer(ans):
    for value in ans[1:]:
        print(value)

def main():
    n = int(get_input())
    tree = initialize_tree(n)
    read_edges(tree, n)
    ans = initialize_ans(n)
    que = initialize_queue(tree)
    process_queue(que, tree, ans)
    print_answer(ans)

main()