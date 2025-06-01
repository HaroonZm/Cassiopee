import sys
import os
import math

def freq_op(A):
    from collections import Counter
    freq = Counter(A)
    return [freq[x] for x in A]

def main():
    for line in sys.stdin:
        try:
            n = int(line.strip())
        except ValueError:
            continue
        if n == 0:
            break
        A = list(map(int, input().split()))
        cnt = 0
        while True:
            B = freq_op(A)
            cnt += 1
            if B == A:
                break
            A = B
        print(cnt-1)
        print(*A)

if __name__ == '__main__':
    main()