def main():
    m, k = map(int, input().split())

    max_a = pow(2, m)

    if k >= max_a:
        print(-1)
        exit()

    if m == 0:
        print('0 0')
        exit()

    if m == 1:
        if k == 0:
            print('0 0 1 1')
        else:
            print(-1)
        exit()

    l = [0] * (2 * max_a)
    l[0] = k
    l[max_a] = k
    for i in range(k):
        l[i + 1] = i
        l[-i - 1] = i
    for i in range(k + 1, max_a):
        l[i] = i
        l[-i] = i
    print(' '.join(map(str, l)))

main()