from itertools import combinations as comb

def cube_dist(a, b):
    return sum([(a[i] - b[i]) ** 2 for i in range(3)])

def cal_total_dist(t):
    if len(t) == 1:
        return 0
    return sum([cube_dist(ca, cb) for ca, cb in comb(t, 2)])

N, M = map(int, raw_input().split())
color = [tuple(map(float, raw_input().split())) for i in range(N)]
print max([cal_total_dist(ctuple) for ctuple in comb(color, M)])