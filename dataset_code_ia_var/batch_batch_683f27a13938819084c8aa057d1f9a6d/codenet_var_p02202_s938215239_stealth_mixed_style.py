n = int(input())
a = [int(x) for x in input().split()]
def calc_diff(seq, num):
    s = 0
    idx = 0
    while idx < len(seq):
        s += seq[idx]
        idx += 1
    total = 0
    for j in range(1, num+1):
        total = total + j
    return s - total
print(calc_diff(a, n))