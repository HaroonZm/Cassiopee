import sys

def set_input_and_recursion_limit():
    reader = (s.rstrip() for s in sys.stdin)
    input_func = reader.__next__
    sys.setrecursionlimit(10**9)
    return input_func

def read_n(input_func):
    return int(input_func())

def init_graph(n):
    return [[] for _ in range(n)]

def read_edge(input_func):
    a, b = map(int, input_func().split())
    return a - 1, b - 1

def build_graph(n, G, input_func):
    for _ in range(n - 1):
        a, b = read_edge(input_func)
        G[a].append(b)
        G[b].append(a)
    return G

def init_flag(n):
    return [0] * n

def set_flag(flag, idx, value):
    flag[idx] = value

def get_neighbors(G, node):
    return G[node]

def dfs_visit(G, flag, cur, par, f):
    set_flag(flag, cur, f)
    for to in get_neighbors(G, cur):
        if to != par:
            dfs_visit(G, flag, to, cur, f ^ 1)

def run_dfs(G, flag):
    dfs_visit(G, flag, 0, -1, 0)

def count_flag(flag):
    return sum(flag)

def count_complement(n, a):
    return n - a

def init_mod_classes():
    return [], [], []

def append_mod_class(i, one, two, three):
    if i % 3 == 0:
        three.append(i)
    elif i % 3 == 1:
        one.append(i)
    else:
        two.append(i)

def mod_classify(n):
    one, two, three = init_mod_classes()
    for i in range(1, n + 1):
        append_mod_class(i, one, two, three)
    return one, two, three

def calc_k(n):
    return n // 3

def init_answer_array(n):
    return [0] * n

def pop_from(lst):
    return lst.pop() if lst else None

def assign_ans_case1(n, flag, one, two, three, ans):
    for i in range(n):
        if flag[i]:
            v = pop_from(one)
            if v is not None:
                ans[i] = v
            else:
                ans[i] = pop_from(three)
        else:
            v = pop_from(two)
            if v is not None:
                ans[i] = v
            else:
                ans[i] = pop_from(three)
    return ans

def concat_classes(one, two, three):
    return one + two + three

def assign_ans_case2a(n, flag, three, one, two, ans):
    for i in range(n):
        if flag[i]:
            ans[i] = pop_from(three)
    res = concat_classes(one, two, three)
    for i in range(n):
        if not flag[i]:
            ans[i] = res.pop()
    return ans

def assign_ans_case2b(n, flag, three, one, two, ans):
    for i in range(n):
        if not flag[i]:
            ans[i] = pop_from(three)
    res = concat_classes(one, two, three)
    for i in range(n):
        if flag[i]:
            ans[i] = res.pop()
    return ans

def main():
    input_func = set_input_and_recursion_limit()
    n = read_n(input_func)
    G = init_graph(n)
    G = build_graph(n, G, input_func)
    flag = init_flag(n)
    run_dfs(G, flag)
    a = count_flag(flag)
    b = count_complement(n, a)
    one, two, three = mod_classify(n)
    k = calc_k(n)
    ans = init_answer_array(n)
    if k < a and k < b:
        ans = assign_ans_case1(n, flag, one, two, three, ans)
    else:
        if k >= a:
            ans = assign_ans_case2a(n, flag, three, one, two, ans)
        else:
            ans = assign_ans_case2b(n, flag, three, one, two, ans)
    print_output(ans)

def print_output(ans):
    print(*ans)

main()