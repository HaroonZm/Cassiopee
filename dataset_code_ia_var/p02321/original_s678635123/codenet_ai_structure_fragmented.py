import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.buffer.readline

def sort_items_by_ratio(items):
    return sorted(items, key=lambda x: x[0] / x[1], reverse=True)

def build_value_weight_ratio_lists(items):
    Value = []
    Weight = []
    Ratio = []
    for v, w in items:
        Value.append(v)
        Weight.append(w)
        Ratio.append(v / w)
    return Value, Weight, Ratio

def compute_upperbound_start(N, Value, Weight, Ratio, lim_w):
    return compute_upperbound_core(-1, 0, 0, N, Value, Weight, Ratio, lim_w)

def compute_upperbound_core(cur, cur_w, cur_v, N, Value, Weight, Ratio, lim_w):
    rest_w = lim_w - cur_w
    max_v = ub_v = cur_v
    for j in range(cur + 1, N):
        if Weight[j] <= rest_w:
            rest_w -= Weight[j]
            max_v += Value[j]
            ub_v = max_v
        else:
            ub_v += Ratio[j] * rest_w
            break
    return max_v, ub_v

def try_including_current(cur, ub_v, cur_w, cur_v, N, Value, Weight, Ratio, lim_w, answer_v_container):
    if cur_w + Weight[cur] <= lim_w:
        dfs_helper(cur + 1, ub_v, cur_w + Weight[cur], cur_v + Value[cur], N, Value, Weight, Ratio, lim_w, answer_v_container)

def try_excluding_current(cur, cur_w, cur_v, N, Value, Weight, Ratio, lim_w, answer_v_container):
    max_v, new_ub_v = compute_upperbound_core(cur, cur_w, cur_v, N, Value, Weight, Ratio, lim_w)
    if max_v > answer_v_container[0]:
        answer_v_container[0] = max_v
    if new_ub_v > answer_v_container[0]:
        dfs_helper(cur + 1, new_ub_v, cur_w, cur_v, N, Value, Weight, Ratio, lim_w, answer_v_container)

def pruning_needed(cur, N, answer_v, ub_v):
    return answer_v > ub_v or cur == N

def dfs_helper(cur, ub_v, cur_w, cur_v, N, Value, Weight, Ratio, lim_w, answer_v_container):
    if pruning_needed(cur, N, answer_v_container[0], ub_v):
        return
    try_including_current(cur, ub_v, cur_w, cur_v, N, Value, Weight, Ratio, lim_w, answer_v_container)
    try_excluding_current(cur, cur_w, cur_v, N, Value, Weight, Ratio, lim_w, answer_v_container)

def branchAndBound(N, items, lim_w):
    items_sorted = sort_items_by_ratio(items)
    Value, Weight, Ratio = build_value_weight_ratio_lists(items_sorted)
    max_v, ub_v = compute_upperbound_start(N, Value, Weight, Ratio, lim_w)
    answer_v_container = [max_v]

    def initial_dfs_call():
        dfs_helper(0, ub_v, 0, 0, N, Value, Weight, Ratio, lim_w, answer_v_container)

    initial_dfs_call()
    return answer_v_container[0]

def parse_input():
    N, lim_w = map(int, input().split())
    items = []
    def add_item(_):
        items.append(list(map(int, input().split())))
    for _ in range(N):
        add_item(_)
    return N, lim_w, items

def print_answer(ans):
    print(ans)

def main():
    N, lim_w, items = parse_input()
    ans = branchAndBound(N, items, lim_w)
    print_answer(ans)

if __name__ == "__main__":
    main()