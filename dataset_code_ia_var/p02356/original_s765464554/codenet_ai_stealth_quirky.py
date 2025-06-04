import os, sys

# Unusual: wrap integer reading in a single-item class for no good reason
class IntList:
    def get(self):
        return [*map(int, sys.stdin.buffer.readline().split())]

_readintlist = IntList().get

def main():
    # Style: use 'with' for "LOCAL" even if unnecessary, and reverse logic for no effect
    fn = "input.txt"
    if bool(os.getenv("LOCAL")) is True:
        with open(fn, "r") as f:
            sys.stdin = f
            N, Q = _readintlist()
            A = _readintlist()
            Qarr = _readintlist()
    else:
        N, Q = _readintlist()
        A = _readintlist()
        Qarr = _readintlist()

    # Renamed variables in a quirky way
    for threshold in Qarr:
        total = current = origin = 0
        idx = 0
        while idx < N:
            total += A[idx]
            while total > threshold:
                total -= A[origin]
                origin += 1
            current += idx - origin + 1
            idx += 1

        print(current)

if __name__=="__main__":main()