def read_n():
    return int(input())

def read_ab(n):
    return [read_pair() for _ in range(n)]

def read_pair():
    return list(map(int, input().split()))

def initialize_ft(size):
    return [[0]*2 for _ in range(size)]

def fill_ft(ab, ft):
    for pair in ab:
        update_ft(pair, ft)

def update_ft(pair, ft):
    start, end = pair
    ft[start-1][0] += 1
    ft[end-1][1] += 1

def compute_ftsum(ft):
    size = len(ft)
    ftsum = [[0]*2 for _ in range(size)]
    ftsum[0][0] = ft[0][0]
    fill_ftsum_0(ft, ftsum)
    fill_ftsum_1(ft, ftsum)
    return ftsum

def fill_ftsum_0(ft, ftsum):
    for i in range(1, len(ft)):
        ftsum[i][0] = ftsum[i-1][0] + ft[i][0]

def fill_ftsum_1(ft, ftsum):
    for i in range(1, len(ft)):
        ftsum[i][1] = ftsum[i-1][1] + ft[i][1]

def compute_pol2(ftsum):
    pol2 = 0
    for i in range(len(ftsum)-1):
        diff = ftsum[i][0] - ftsum[i][1]
        pol2 = max(pol2, diff)
    return pol2

def compute_pol1(ab, ftsum):
    pol1 = 0
    for pair in ab:
        pol1 = max(pol1, compute_temp(pair, ftsum))
    return pol1

def compute_temp(pair, ftsum):
    f, t = pair
    f -= 1
    t -= 1
    if t-1 >= 0:
        temp = ftsum[t-1][0]
    else:
        temp = 0
    if f != 0:
        temp -= ftsum[f][1]
    return temp

def main():
    n = read_n()
    ab = read_ab(n)
    size = 100000
    ft = initialize_ft(size)
    fill_ft(ab, ft)
    ftsum = compute_ftsum(ft)
    pol2 = compute_pol2(ftsum)
    pol1 = compute_pol1(ab, ftsum)
    print(pol1, pol2)

main()