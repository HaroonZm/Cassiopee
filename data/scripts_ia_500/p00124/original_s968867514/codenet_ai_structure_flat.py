import sys
sys.setrecursionlimit(100000)
BIG_NUM = 2000000000
HUGE_NUM = 99999999999999999
MOD = 1000000007
EPS = 0.000000001
is_First = True
while True:
    N = int(input())
    if N == 0:
        break
    if not is_First:
        print()
    table = []
    i = 0
    while i < N:
        tmp = input().split()
        tmp_name = tmp[0]
        win = int(tmp[1])
        lose = int(tmp[2])
        draw = int(tmp[3])
        value = 3 * win + draw
        table.append((tmp_name, i, value))
        i += 1
    j = 0
    while j < N - 1:
        k = j + 1
        while k < N:
            # Compare and swap if needed
            if (table[j][2] < table[k][2]) or (table[j][2] == table[k][2] and table[j][1] > table[k][1]):
                table[j], table[k] = table[k], table[j]
            k += 1
        j += 1
    l = 0
    while l < N:
        print(f"{table[l][0]},{table[l][2]}")
        l += 1
    is_First = False