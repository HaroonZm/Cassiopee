# AOJ 2199 - 差分パルス符号変調
# 配るDP
import sys

def main():
    inf = float('inf')
    error_list = tuple(tuple((i - j) ** 2 for i in range(256)) for j in range(256))

    while True:
        N, M = map(int, sys.stdin.readline().strip().split())

        if N == 0:
            break

        C = tuple(int(sys.stdin.readline()) for _ in range(M))

        decode_list = tuple(tuple(255 if j + c > 255 else 0 if j + c < 0 else j + c for c in C) for j in range(256))

        # dp 初期化 ---------------------------------------------------------
        dp1 = [inf] * 256
        dp1[128] = 0

        # dp 計算 ---------------------------------------------------------
        for _ in range(N):
            x = int(sys.stdin.readline())
            error_list_x = error_list[x]
            dp2 = [inf] * 256

            for decode_list_j, dp1_j in zip(decode_list, dp1):
                for x_decode in decode_list_j:

                    new_sum_error = dp1_j + error_list_x[x_decode]

                    if new_sum_error < dp2[x_decode]:
                        dp2[x_decode] = new_sum_error

            dp1 = dp2[:]

        print(min(dp1))

if __name__ == '__main__':
    main()