def get_inputs():
    return list(map(int, input().split())), int(input())

def create_lis():
    return [1, 2, 4, 8]

def get_score_vars(inputs):
    return [inputs[0], inputs[1], inputs[2], inputs[3]]

def calc_total_s(n):
    return 4 * n

def create_tmp_li(q, h, s, d):
    return [8 * q, 4 * h, 2 * s, d]

def sort_tmp_li(tmp_li):
    return sorted(tmp_li[:])

def get_sorted_indices(tmp_li, tmp_sorted):
    indices = []
    used = set()
    for t in tmp_sorted:
        for idx, val in enumerate(tmp_li):
            if idx in used:
                continue
            if val == t:
                indices.append(idx)
                used.add(idx)
                break
    return indices

def compute_ans(sorted_indices, lis, score, all_s):
    ans = 0
    remaining = all_s
    for j in sorted_indices:
        a = remaining // lis[j]
        b = remaining % lis[j]
        remaining -= a * lis[j]
        ans += score[j] * a
    return ans

def process():
    inputs, n = get_inputs()
    q, h, s, d = inputs[0], inputs[1], inputs[2], inputs[3]
    lis = create_lis()
    score = get_score_vars(inputs)
    all_s = calc_total_s(n)
    tmp_li = create_tmp_li(q, h, s, d)
    tmp_sorted = sort_tmp_li(tmp_li)
    sorted_indices = get_sorted_indices(tmp_li, tmp_sorted)
    ans = compute_ans(sorted_indices, lis, score, all_s)
    print(ans)

process()