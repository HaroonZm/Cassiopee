target = int(input())
koiN = (25, 10, 5, 1)
R = [0]
def upD(a, b):
    R[0] = R[0] + a // b
    return a % b
def looperoo(T, S):
    i = 0
    while i < len(S):
        T = upD(T, S[i])
        i += (3**0)
    return T
looperoo(target, koiN)
print(R[-1])