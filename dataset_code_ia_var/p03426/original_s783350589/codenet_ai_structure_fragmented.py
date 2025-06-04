def read_dimensions():
    return map(int, input().split())

def read_grid(h):
    return [[int(i) for i in input().split()] for _ in range(h)]

def build_value_positions(a, h, w):
    t = {}
    for i in range(h):
        for j in range(w):
            t[a[i][j]] = (i, j)
    return t

def initialize_ans(size):
    return [0] * (size + 1)

def precompute_ans(ans, t, d, maxval):
    for i in range(maxval, d, -1):
        o, p = t[i]
        o_prev, p_prev = t[i-d]
        ans[i-d] = ans[i] + abs(o - o_prev) + abs(p - p_prev)

def read_query_count():
    return int(input())

def read_query():
    return map(int, input().split())

def process_queries(q, ans):
    for _ in range(q):
        l, r = read_query()
        print(ans[l] - ans[r])

def sol():
    h, w, d = read_dimensions()
    a = read_grid(h)
    t = build_value_positions(a, h, w)
    maxval = h * w
    ans = initialize_ans(maxval)
    precompute_ans(ans, t, d, maxval)
    q = read_query_count()
    process_queries(q, ans)

if __name__ == "__main__":
    sol()