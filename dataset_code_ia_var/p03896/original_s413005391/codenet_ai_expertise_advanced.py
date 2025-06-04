import sys
import numpy as np

def input(): return sys.stdin.readline()

def construct_latin_square(N):
    if N == 2:
        return None
    if N == 4:
        return np.array([[3, 2, 4],
                         [3, 4, 1],
                         [4, 1, 2],
                         [2, 1, 3]], dtype=np.int32)
    if N % 2 == 1:
        indices = np.add.outer(np.arange(N), np.arange(1, N + 1)) % N + 1
        return indices
    # N even and greater than 4
    M = N // 2
    top_left = construct_latin_square(M)
    result = np.empty((N, N - 1), dtype=np.int32)
    result[:M, :M-1] = top_left
    result[M:, :M-1] = top_left + M
    for idx in range(M - 1, N - 1):
        result[:M, idx]   = (np.arange(M) + idx) % M + M + 1
        result[M:, idx]   = (np.arange(M) + (1-idx)) % M + 1
    return result

def main():
    N = int(input())
    out = construct_latin_square(N)
    if out is None:
        print(-1)
        return
    # Printing using efficient vectorized string conversion
    print('\n'.join(' '.join(map(str, row)) for row in out))

if __name__ == '__main__':
    main()