case = 1
while True:
    n = int(input())
    if not n:
        break
    jpeg = [[0] * n for _ in range(n)]
    n1 = n - 1
    px, cur = [0, 0], 1
    while px[0] < n:
        i, j = px
        jpeg[i][j] = cur
        odd = (i + j) % 2
        if px[not odd] == n1:
            px[odd] += 1
        elif not px[odd]:
            px[not odd] += 1
        else:
            px[not odd] += 1
            px[odd] -= 1
        cur += 1

    print('Case {}:'.format(case))
    for row in jpeg:
        print(''.join('{:>3}'.format(pixel) for pixel in row))

    case += 1