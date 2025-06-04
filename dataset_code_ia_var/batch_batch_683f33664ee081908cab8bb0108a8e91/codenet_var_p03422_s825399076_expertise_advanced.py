import sys
import numpy as np

def main():
    N = int(sys.stdin.readline())
    data = np.fromstring(sys.stdin.read(), dtype=np.int32, sep=' ')
    A, K = data[::2], data[1::2]

    G = 0
    mask = np.ones_like(A, dtype=bool)

    for t in range(0, 50000, 1000):
        for _ in range(1000):
            q = (A // K) + 1
            r = A % K
            A -= r + (-r) % q

        terminal = (A % K == 0)
        if np.any(terminal):
            G ^= np.bitwise_xor.reduce(A[terminal] // K[terminal])
            keep = ~terminal
            if not np.any(keep):
                break
            A, K = A[keep], K[keep]

    print('Takahashi' if G else 'Aoki')

if __name__ == '__main__':
    main()