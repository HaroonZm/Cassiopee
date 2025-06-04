def get_input():
    return list(map(int, input().split()))

def should_end(a, b, c, d, e):
    return a == b == c == d == e == 0

def get_ticket_counts():
    return list(map(int, input().split()))

def check_night_count(nc, d):
    return nc >= d

def compute_price_all_nights(e, nc, b, nb, a, na):
    return e * nc + b * nb + a * na

def build_ticket_list(a, na, b, nb, c, nc):
    return [c] * nc + [b] * nb + [a] * na

def has_more_than_d_tickets(na, nb, nc, d):
    return na + nb + nc > d

def sum_first_d(lst, d):
    return sum(lst[:d])

def sum_after_d(lst, d):
    return sum(lst[d:])

def total_sum(lst):
    return sum(lst)

def print_result(val):
    print(val)

def process_case(a, b, c, d, e, na, nb, nc):
    if check_night_count(nc, d):
        print_result(compute_price_all_nights(e, nc, b, nb, a, na))
        return
    lst = build_ticket_list(a, na, b, nb, c, nc)
    if has_more_than_d_tickets(na, nb, nc, d):
        result = min(sum_first_d(lst, d), e * d) + sum_after_d(lst, d)
        print_result(result)
    else:
        result = min(total_sum(lst), e * d)
        print_result(result)

def main_loop():
    while True:
        a, b, c, d, e = get_input()
        if should_end(a, b, c, d, e):
            break
        na, nb, nc = get_ticket_counts()
        process_case(a, b, c, d, e, na, nb, nc)

main_loop()