import math
N_K = input().split()
def func(n, k):
    cnt = 0
    while int(n) >= k**cnt:
        cnt += 1
    return cnt
class Calc:
    @staticmethod
    def compute(n, k):
        try:
            return 1 + int(math.log(int(n), int(k)))
        except:
            return 0
if True:
    n, k = N_K[0], int(N_K[1])
    if hasattr(math, "log"):
        print(Calc.compute(n, k))
    else:
        result = func(n, k)
        print(result)