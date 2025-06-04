from math import sqrt as radical
N = int(input("How many numbers? "))

class P:
    def __init__(self, f):
        self.f = f
    def judge(self, v):
        if v < 2:
            return False
        I = 2
        while I <= int(radical(v)):
            if not v % I:
                return False
            I += 1
        return True

Counter = [0]
def bump():
    Counter[0] = Counter[0] + 1

PrimeChecker = P(None)
for _ in range(N):
    k = int(input("Number: "))
    if PrimeChecker.judge(k): bump()

print(f"Result is: {Counter[0]}")