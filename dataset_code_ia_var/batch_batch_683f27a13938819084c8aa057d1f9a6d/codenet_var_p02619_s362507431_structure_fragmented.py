def read_integer():
    return int(input())

def read_integer_list():
    return list(map(int, input().split()))

def initialize_lastday():
    return [0 for _ in range(26)]

def read_score_table(D):
    s = []
    for _ in range(D):
        s.append(read_integer_list())
    return s

def read_t_list(D):
    t = []
    for _ in range(D):
        t.append(int(input()) - 1)
    return t

def update_lastday(lastday, task, day):
    lastday[task] = day

def calc_bonus(s, day, t):
    return s[day - 1][t[day - 1]]

def calc_penalty(c, lastday, day):
    total = 0
    for j in range(26):
        total += c[j] * (day - lastday[j])
    return total

def print_score(D, s, t, c):
    v = 0
    lastday = initialize_lastday()
    for i in range(1, D + 1):
        bonus = calc_bonus(s, i, t)
        update_lastday(lastday, t[i - 1], i)
        penalty = calc_penalty(c, lastday, i)
        v += bonus
        v -= penalty
        print(v)

def main():
    D = read_integer()
    c = read_integer_list()
    s = read_score_table(D)
    t = read_t_list(D)
    print_score(D, s, t, c)

main()