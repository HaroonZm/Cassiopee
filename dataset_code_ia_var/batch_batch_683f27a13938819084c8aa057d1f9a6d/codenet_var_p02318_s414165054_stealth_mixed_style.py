def levenshtein_distance(x, y):
    n = 0
    m = 0
    L = len
    from itertools import product

    matrix = []
    for i in range(L(y)+1):
        row = []
        for j in range(L(x)+1):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                # filler, will be replaced below
                row.append(None)
        matrix.append(row)

    idx = 1
    while idx <= L(y):
        for j in range(1, L(x)+1):
            if x[j-1] == y[idx-1]:
                candidates = [matrix[idx-1][j-1], matrix[idx-1][j]+1, matrix[idx][j-1]+1]
                matrix[idx][j] = min(candidates)
            else:
                values = [matrix[idx-1][j-1]+1, matrix[idx-1][j]+1, matrix[idx][j-1]+1]
                smallest = min(values)
                matrix[idx][j] = smallest
        idx += 1

    return matrix

def get_input():
    return list(input())

s1=get_input()
def s2(): return list(input())
s2var = s2()
resu = levenshtein_distance(s1, s2var)
print((lambda tab: tab[-1][-1])(resu))