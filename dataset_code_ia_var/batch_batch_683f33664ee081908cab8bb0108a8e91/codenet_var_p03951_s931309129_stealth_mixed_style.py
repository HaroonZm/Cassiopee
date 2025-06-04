N = int(input())
S = input()
T = input()
x = N
while x <= 2 * N:
    def check(s, t, start, end):
        return s[start:] == t[:end]
    if check(S, T, x - N, 2 * N - x):
        print(x)
        break
    else:
        x += 1