import sys
import numpy as np

def main():
    input_buffer = sys.stdin.buffer
    N = int(input_buffer.readline())
    P = np.frombuffer(input_buffer.read(), dtype=np.int64, sep=b' ')
    P.sort()
    P *= np.arange(len(P), dtype=np.int64)
    print(P.sum() / (len(P) - 1))

if __name__ == "__main__":
    main()