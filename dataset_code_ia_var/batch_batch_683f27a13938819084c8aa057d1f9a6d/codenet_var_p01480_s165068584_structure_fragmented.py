def get_input():
    return input()

def allocate_q_list(size):
    return [0]*(size + 1)

def get_iter_range(size):
    return range(size + 1)

def parse_nm_line():
    n, m = map(int, raw_input().split())
    return n, m

def parse_vr_lines(m):
    vr = []
    for _ in range(m):
        line = raw_input().split()
        v, r = map(float, line)
        vr.append((v, r))
    return vr

def compute_weighted_sum(vr):
    return sum([v*r for v, r in vr])

def compute_weight_sum(vr):
    return sum([r for v, r in vr])

def compute_q_element(vr):
    weighted_sum = compute_weighted_sum(vr)
    weight_sum = compute_weight_sum(vr)
    if weight_sum == 0:
        return 0  # Prevent division by zero
    return weighted_sum / weight_sum

def fill_q_list(q, t):
    for i in get_iter_range(t):
        n, m = parse_nm_line()
        vr = parse_vr_lines(m)
        q[i] = compute_q_element(vr)

def subtract_last_q(q, t):
    last_q = q[-1]
    return [q[i] - last_q for i in range(t + 1)]

def print_result(q):
    if max(q) > 0.0000001:
        print "YES"
    else:
        print "NO"

def main():
    t = get_input()
    q = allocate_q_list(t)
    fill_q_list(q, t)
    q_sub = subtract_last_q(q, t)
    print_result(q_sub)

main()