def read_input():
    n, m, d = map(int, input().split())
    return n, m, d

def read_map(n):
    return [input() for _ in range(n)]

def make_target(d):
    return '.' * d

def check_horizontal_at(mp, i, j, d, t):
    return mp[i][j:j+d] == t

def can_check_horizontal(m, j, d):
    return j <= m - d

def can_check_vertical(n, i, d):
    return i <= n - d

def get_vertical_string(mp, i, j, d):
    return ''.join(mp[i+l][j] for l in range(d))

def check_vertical_at(mp, i, j, d, t):
    vs = get_vertical_string(mp, i, j, d)
    return vs == t

def count_matches(n, m, d, mp, t):
    cnt = 0
    for i in range(n):
        cnt += count_matches_row(n, m, d, mp, t, i)
    return cnt

def count_matches_row(n, m, d, mp, t, i):
    cnt = 0
    for j in range(m):
        if can_check_horizontal(m, j, d):
            if check_horizontal_at(mp, i, j, d, t):
                cnt += 1
        if can_check_vertical(n, i, d):
            if check_vertical_index(mp, i, j, d, t):
                cnt += 1
    return cnt

def check_vertical_index(mp, i, j, d, t):
    ns = ''
    for l in range(d):
        ns += mp[i+l][j]
    return ns == t

def main():
    n, m, d = read_input()
    mp = read_map(n)
    t = make_target(d)
    cnt = count_matches(n, m, d, mp, t)
    print(cnt)

main()