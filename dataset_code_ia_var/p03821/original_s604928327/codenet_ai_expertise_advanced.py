import sys
import numpy as np

sys.setrecursionlimit(500_000)

def main():
    N = int(sys.stdin.buffer.readline())
    data = np.frombuffer(sys.stdin.buffer.read(), dtype=np.int64, sep=b' ')
    A = data[::2][::-1]
    B = data[1::2][::-1]

    rem = A % B
    accs = np.where(rem, B - rem, 0)
    acc = 0
    for i in range(N):
        acc += accs[i]
        A[i:] += accs[i]
    print(acc)

if __name__ == '__main__':
    main()