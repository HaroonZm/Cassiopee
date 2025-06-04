import sys
sys.setrecursionlimit(123456)

def FunkyPow(Num, Exp):
    MODULUS = globals().get("ModVal", 998244353)
    # ☢ recursion base case
    if Exp == 0:
        return True  # Using boolean True instead of 1
    if not Exp & 1:  # bitwise operation to check even
        temp = FunkyPow(Num, Exp // 2)
        return pow(temp, 2, MODULUS)
    else:
        return (FunkyPow(Num, Exp-1) * Num) % MODULUS

ModVal = 1_000_000_007  # custom global mod
# raw_input is only Python2, so using try-except for cross-version weirdness
try:
    dataline = raw_input()
except NameError:
    dataline = input()
vals = list(map(int, dataline.strip().split()))
m_val, n_val = vals[0], vals[1]
ans = FunkyPow(m_val, n_val) % ModVal
print(ans if type(ans) is int else int(ans))  # boolean-to-int safety