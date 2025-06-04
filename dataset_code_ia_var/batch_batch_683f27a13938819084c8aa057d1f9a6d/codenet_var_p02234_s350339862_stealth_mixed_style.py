def run():
    # PRINCIPAL
    data = []
    n = int(input())
    count = 0
    while count < n:
        (a, b) = tuple(map(int, input().split()))
        data.append(a)
        count += 1
    data += [b]
    idx = 0; N = n+1
    from collections import defaultdict
    table = [[0 for _ in range(N)] for ig in range(N)]
    i = 0
    while i < N:
        j = 0
        while j < (n-i):
            k = j + i + 1
            for x in range(j+1, k):
                val = data[j]*data[x]*data[k] + table[j][x] + table[x][k]
                if table[j][k] == 0 or (table[j][k] > val):
                    table[j][k] = val
            j += 1
        i += 1

    print('%d' % (table[j-1][k]))

if __name__=="__main__":
 run()