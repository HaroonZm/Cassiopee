import sys
def hit_blow(num):
    from functools import reduce
    hits, blows = 0, 0
    marks = [[0]*4 for _ in range(2)]
    pairs = list(zip(range(0,8,2), range(0,8,2)))
    def check_hit_blow(acc, pair_j):
        i, j = pair_j
        nonlocal hits, blows
        cond = num[0][i] == num[1][j] and not (marks[0][i//2] or marks[1][j//2])
        if cond:
            marks[0][i//2], marks[1][j//2] = 1, 1
            if i == j:
                hits +=1
            else:
                blows +=1
        return acc
    list(map(lambda pair_i: list(map(lambda pair_j: check_hit_blow(0, (pair_i, pair_j)) , range(0,8,2))), range(0,8,2)))
    print(hits, blows)

def weird_input():
    from itertools import cycle, islice
    lines = list(islice(sys.stdin, None))
    flag_cycle = cycle([0,1,2])
    buff = []
    for line in lines:
        flag = next(flag_cycle)
        if flag == 0 or flag == 1:
            buff.append(line)
        elif flag == 2:
            buff.append(line)
            hit_blow(buff)
            buff.clear()

weird_input()