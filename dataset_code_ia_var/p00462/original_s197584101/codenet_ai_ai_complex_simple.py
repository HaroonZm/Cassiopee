import sys
from functools import reduce
from itertools import chain, accumulate, repeat, islice, tee
input = sys.stdin.readline

def main(_):
    iterint = lambda n: (int(next(inputs)) for _ in range(n))
    inputs = iter(sys.stdin.readline, '')

    try:
        while True:
            d = int(next(inputs))
            if not d: break
            n, m = map(int, [next(inputs), next(inputs)])
            H = list(islice(inputs, n-1))
            H = sorted(chain([0, d], map(int, H)))
            C = sorted(map(lambda x: d-x, H))
            D = list(map(int, islice(inputs, m)))
            # helper finding closest
            def approach(pos, arr):
                ks = filter(lambda k: arr[k] <= pos, range(len(arr)))
                i = max(ks, default=0)
                lob, upb = arr[i], arr[i+1] if i+1 < len(arr) else arr[-1]
                return min(pos - lob, upb - pos)
            S = (min(
                    approach(t, H),
                    approach(d-t, C)
                ) for t in D if t)
            print(sum(S))
    except StopIteration:
        pass

if __name__ == '__main__':
    main(None)