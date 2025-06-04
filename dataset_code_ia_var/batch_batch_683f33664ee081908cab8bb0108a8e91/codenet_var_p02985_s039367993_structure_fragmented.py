def read_initial_input():
    n, k = map(int, input().split())
    return n, k

def build_adjacency_list(n):
    ki = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        add_edge(ki, a-1, b-1)
    return ki

def add_edge(ki, a, b):
    ki[a].append(b)
    ki[b].append(a)

def initialize_seen(n, k):
    seen = [-1] * n
    seen[0] = k
    return seen

def initialize_todo():
    from collections import deque
    return deque([0])

def process_tree(n, k, ki, seen, todo):
    while not is_todo_empty(todo):
        t = pop_todo(todo)
        s = get_initial_color_count(k, seen[t])
        for neighbor in get_neighbors(ki, t):
            if is_unvisited(seen, neighbor):
                if not can_paint(s):
                    print_zero_and_exit()
                mark_visited(seen, neighbor, s)
                s = decrement_s(s)
                append_todo(todo, neighbor)

def is_todo_empty(todo):
    return not todo

def pop_todo(todo):
    return todo.popleft()

def get_initial_color_count(k, parent_color_count):
    return max(k-2, parent_color_count-1)

def get_neighbors(ki, t):
    return ki[t]

def is_unvisited(seen, li):
    return seen[li] == -1

def can_paint(s):
    return s > 0

def print_zero_and_exit():
    print(0)
    exit()

def mark_visited(seen, li, s):
    seen[li] = s

def decrement_s(s):
    return s - 1

def append_todo(todo, neighbor):
    todo.append(neighbor)

def compute_final_answer(seen, mod):
    ans = 1
    for s in seen:
        ans = multiply_and_mod(ans, s, mod)
    return ans

def multiply_and_mod(a, b, mod):
    return (a * b) % mod

def main():
    n, k = read_initial_input()
    ki = build_adjacency_list(n)
    mod = pow(10, 9) + 7
    seen = initialize_seen(n, k)
    todo = initialize_todo()
    process_tree(n, k, ki, seen, todo)
    ans = compute_final_answer(seen, mod)
    print(ans)

main()