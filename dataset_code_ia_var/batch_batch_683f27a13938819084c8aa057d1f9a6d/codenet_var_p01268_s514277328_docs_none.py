def eratosthenes(n):
    length = 150000
    ret = []
    flag = [True] * length
    for i in range(2, length):
        if flag[i]:
            if n < i:
                ret.append(i)
            for j in range(i, length, i):
                flag[j] = False
        if len(ret) > 50:
            break
    return ret

if __name__ == "__main__":
    while True:
        N, P = map(int, input().split())
        if N == -1 and P == -1:
            break
        ret = eratosthenes(N)
        sosu_add = []
        for i in range(len(ret)):
            for j in range(i, len(ret)):
                sosu_add.append(ret[i] + ret[j])
        sosu_add.sort()
        print(sosu_add[P - 1])