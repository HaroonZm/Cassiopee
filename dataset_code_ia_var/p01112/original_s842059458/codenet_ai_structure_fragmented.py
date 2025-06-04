from collections import defaultdict

def read_int():
    return int(input())

def read_pair():
    return map(int, input().split())

def get_m():
    return read_int()

def get_all_pairs(n):
    d = defaultdict(int)
    k = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            d[k] = (i, j)
            k += 1
    return d, k

def get_p(m):
    p = defaultdict(int)
    for _ in range(m):
        x, y = read_pair()
        p[(x, y)] = 1
        p[(y, x)] = -1
    return p

def create_initial_ans(n):
    ans = defaultdict(int)
    tmp = [0] * n
    ans[tuple(tmp)] = 1
    return ans

def process_favored(i, d, p, ans, n):
    nd = defaultdict(int)
    for key, value in ans.items():
        key = list(key)
        x, y = d[i]
        if p[(x, y)] == 1:
            if key[x - 1] == n // 2:
                continue
            key[x - 1] += 1
            nd[tuple(key)] += value
        else:
            if key[y - 1] == n // 2:
                continue
            key[y - 1] += 1
            nd[tuple(key)] += value
    return nd

def process_unfavored(x, y, key, n, value, nd):
    if key[y - 1] != n // 2:
        key[y - 1] += 1
        nd[tuple(key)] += value
        key[y - 1] -= 1
    if key[x - 1] != n // 2:
        key[x - 1] += 1
        nd[tuple(key)] += value

def process_no_preference(i, d, p, ans, n):
    nd = defaultdict(int)
    for key, value in ans.items():
        key = list(key)
        x, y = d[i]
        process_unfavored(x, y, key, n, value, nd)
    return nd

def update_ans(i, d, p, ans, n):
    nd = defaultdict(int)
    for key, value in ans.items():
        key = list(key)
        x, y = d[i]
        if p[(x, y)]:
            if p[(x, y)] == 1:
                if key[x - 1] == n // 2:
                    continue
                key[x - 1] += 1
                nd[tuple(key)] += value
            else:
                if key[y - 1] == n // 2:
                    continue
                key[y - 1] += 1
                nd[tuple(key)] += value
        else:
            process_unfavored(x, y, key, n, value, nd)
    return nd

def calculate_ans(n, k, d, p):
    ans = create_initial_ans(n)
    for i in range(k):
        ans = update_ans(i, d, p, ans, n)
    return ans

def output(ans, n):
    print(ans[tuple([n // 2] * n)])

def main(n):
    m = get_m()
    d, k = get_all_pairs(n)
    p = get_p(m)
    ans = calculate_ans(n, k, d, p)
    output(ans, n)

def process_input():
    while True:
        n = read_int()
        if n:
            main(n)
        else:
            break

if __name__ == "__main__":
    process_input()