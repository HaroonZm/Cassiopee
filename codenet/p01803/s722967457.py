from sys import exit, stderr, stdin
input = stdin.readline
# setrecursionlimit(10**7)

def debug(var, name="hoge"):
    print(str(type(var)) + name +":" + " = " + repr(var), file=stderr)
    return
NUM = 100
MOD = 10 ** 16 + 61
base = 12345
base_inv = pow(base,MOD-2,MOD)
power = [1] * NUM
power_inv = [1] * NUM
for n in range(1,NUM):
    power[n] = power[n-1] * base % MOD
    power_inv[n] = power_inv[n-1] * base_inv % MOD
def rollhash(s):
    res = [0]*(len(s)+1)
    for i in range(len(s)):
        res[i+1] = (res[i] + power[i] * ord(s[i])) % MOD
    return res

def main():
    while(1):
        N = int(input())
        if (N == 0):
            break
        S = []
        mL = 0
        for _ in range(N):
            s = (input().rstrip())
            n = ''
            for i in range(len(s)-1):
                if s[i] in {'a', 'i', 'u', 'e', 'o'}:
                    n += s[i+1]
            n = s[0] + n
            S.append(n)
        S = sorted(S, key=lambda x: -len(x))
        # print(S)
        if len(set(S)) < N:
            print(-1)
            continue
        for k in range(1,51):
            kind = set()
            for s in S:
                kind.add(s[:k])
            if len(kind) == N:
                break
        if len(kind) == N:
            print(k)

if __name__ == "__main__":
    main()