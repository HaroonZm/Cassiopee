def main_loop():
    while True:
        values = get_input()
        if is_termination(values[0]):
            break
        abc_counts = get_counts()
        result = process_case(values, abc_counts)
        print_result(result)

def get_input():
    return list(map(int, raw_input().split()))

def is_termination(a):
    return a == 0

def get_counts():
    return list(map(int, raw_input().split()))

def process_case(values, counts):
    a, b, c, d, e = values
    na, nb, nc = counts
    t = compute_total_count(na, nb, nc)
    ans = compute_initial_answer(na, nb, nc, a, b, c)
    if is_less_than_d(t, d):
        ans = minimum_ans_when_under_d(ans, d, e)
    else:
        ans = process_when_t_greater_equal_d(na, nb, nc, d, a, b, c, e)
    return ans

def compute_total_count(na, nb, nc):
    return na + nb + nc

def compute_initial_answer(na, nb, nc, a, b, c):
    return na*a + nb*b + nc*c

def is_less_than_d(t, d):
    return t < d

def minimum_ans_when_under_d(ans, d, e):
    if ans > d*e:
        return d*e
    return ans

def process_when_t_greater_equal_d(na, nb, nc, d, a, b, c, e):
    tmp = 0
    dd = d
    cnt = 0
    cnt, dd = process_by_type(cnt, dd, nc, c)
    cnt, dd = process_by_type(cnt, dd, nb, b)
    cnt, dd = process_by_type(cnt, dd, na, a)
    if cnt >= d * e:
        a, b, c = set_minimum_prices(a, b, c, e)
        cnt = reprocess_cnt_with_e(na, nb, nc, d, a, b, c, e)
        return cnt
    else:
        return cnt

def process_by_type(cnt, dd, n, price):
    if dd >= n:
        cnt += n * price
        dd -= n
    else:
        cnt += dd * price
        dd = 0
    return cnt, dd

def set_minimum_prices(a, b, c, e):
    a = min_price(a, e)
    b = min_price(b, e)
    c = min_price(c, e)
    return a, b, c

def min_price(orig, e):
    if e < orig:
        return e
    return orig

def reprocess_cnt_with_e(na, nb, nc, d, a, b, c, e):
    dd = d
    cnt = 0
    cnt, dd = process_by_type_with_min(cnt, dd, nc, e, c)
    cnt, dd = process_by_type_with_min(cnt, dd, nb, e, b)
    cnt, dd = process_by_type_with_min(cnt, dd, na, e, a)
    return cnt

def process_by_type_with_min(cnt, dd, n, e, val):
    if dd >= n:
        cnt += n * e
        dd -= n
    else:
        cnt += dd * e
        cnt += (n - dd) * min(e, val)
        dd = 0
    return cnt, dd

def print_result(ans):
    print ans

main_loop()