def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    dx = [0, 1, -1, 0, 0]
    dy = [0, 0, 0, 1, -1]

    for _ in range(n):
        A = [list(map(int, input().split())) for __ in range(10)]
        B = [[0]*10 for __ in range(10)]

        for i in range(9):
            for j in range(10):
                if A[i][j] == 1:
                    B[i+1][j] ^= 1
                    for k in range(5):
                        ni = i + dy[k]
                        nj = j + dx[k]
                        if 0 <= ni < 10 and 0 <= nj < 10:
                            A[ni][nj] ^= 1

        for j in range(10):
            B[0][j] = A[0][j]

        for row in B:
            print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()