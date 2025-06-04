import itertools as ite
import math

def get_input_values():
    N, M = map(int, raw_input().split())
    m = map(int, raw_input().split())
    Q = input()
    l = map(int, raw_input().split())
    return N, M, m, Q, l

def add_sentinel(m, N):
    return m + [N + 1]

def make_cost_array(N):
    return [0] * (N + 1)

def update_cost_for_m(cost, m, M, N):
    for i in range(M):
        idx = m[i + 1] - m[i] - 1
        cost[idx] += 1
    cost[N] += m[0] - 1

def reverse_iterator(N):
    return range(N - 1, -1, -1)

def compute_gradient(cost, N):
    grad = 0
    for i in reverse_iterator(N):
        grad += cost[i]
        cost[i] = cost[i + 1] + grad

def build_dictionary(cost, N):
    dic = {}
    S = 10 ** 5 + 1
    for i in range(1, N + 1):
        if S != cost[i]:
            for j in range(cost[i], S):
                dic[j] = i
            S = cost[i]
    return dic

def print_results(l, dic):
    for num in l:
        if not num in dic:
            print -1
        else:
            print dic[num]

def main():
    N, M, m, Q, l = get_input_values()
    m = add_sentinel(m, N)
    cost = make_cost_array(N)
    update_cost_for_m(cost, m, M, N)
    compute_gradient(cost, N)
    dic = build_dictionary(cost, N)
    print_results(l, dic)

main()