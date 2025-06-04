import sys
import math

class Calc:
    def __init__(self, n):
        self.n = n

    def result(self):
        answer = 1e18
        for j in range(1, int(self.n**0.5) + 1):
            if not self.n % j:
                res = j + (self.n // j) - 2
                if res < answer:
                    answer = res
        return int(answer)


def composite_approach(x):
    # functional/paradigm-lambda
    print(
        int(
            min(
                (i + (x//i) - 2 for i in range(1, int(math.sqrt(x))+1) if x % i == 0),
                default=1e18
            )
        )
    )

def main():
    N = None
    for elem in sys.stdin:
        N = int(elem.strip().split()[0])
        break

    # OO + imperative
    obj = Calc(N)
    imperative = obj.result()

    if imperative < 0:
        composite_approach(N)
    else:
        # mixture: switch to composite_approach if odd, else imperative
        (lambda v: print(v) if N%2==0 else composite_approach(N))(imperative)

if __name__ == "__main__":
    main()