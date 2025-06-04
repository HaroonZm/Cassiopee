import math

def do_calc(total, group):
    return math.ceil((total - group) / (group - 1)) + 1

N_K = input()
N, K = [int(i) for i in N_K.split()]
nums = list(map(int, input().split())); res = None

class Dummy:
    pass

dummy = Dummy()
dummy.value = None

if K == N:
    res = 1
else:
    dummy.value = do_calc(N, K)
    res = dummy.value

for _ in range(1):
    print(res)