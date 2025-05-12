import sys
def main():
    L, N = map(int, input().split())
    lines = sys.stdin.readlines()

    trees_ccw = [None] * N
    for i in range(N):
        trees_ccw[i] = int(lines[i])

    trees_cw = [L - trees_ccw[-(i+1)] for i in range(N)]
    trees_ccw_accum = [0] + [None] * N
    trees_cw_accum = [0] + [None] * N
    for i in range(N):
        trees_ccw_accum[i+1] = trees_ccw_accum[i] + trees_ccw[i]
        trees_cw_accum[i+1] = trees_cw_accum[i] + trees_cw[i]

    #print(trees_ccw)
    #print(trees_cw)
    #print(trees_ccw_accum)
    #print(trees_cw_accum)

    dist_max = 0

    for i in range(1,N+1):
        offset_left = i
        n_left = offset_left + (N-offset_left) // 2 #ccwの数
        n_right = N - n_left    #cwの数

        '''
        [print('L', end='') for _ in range(offset_left-1)]
        print('L', end='_')
        for i_ in range(N-offset_left):
            if i_ % 2 == 0:
                print('R', end='')
            else:
                print('L', end='')
        print()
        print(offset_left, n_left, n_right)
        '''

        dist_1 = 2 * (trees_ccw_accum[n_left] - trees_ccw_accum[i-1]) + 2 * trees_cw_accum[n_right]
        dist_2 = 2 * (trees_cw_accum[n_left] - trees_cw_accum[i-1]) + 2 * trees_ccw_accum[n_right]

        if (N-offset_left) % 2 == 0:
            dist_1 -= trees_ccw[n_left-1]
            dist_2 -= trees_cw[n_left-1]
        else:
            dist_1 -= trees_cw[n_right-1]
            dist_2 -= trees_ccw[n_right-1]

        if dist_max < dist_1:
            dist_max = dist_1

        if dist_max < dist_2:
            dist_max = dist_2

        #print(n_left, dist_1, dist_2, dist_max)

    print(dist_max)
    return

main()