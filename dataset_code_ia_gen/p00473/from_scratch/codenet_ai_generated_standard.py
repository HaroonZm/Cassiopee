N = int(input())
t = [int(input()) for _ in range(N - 1)]
pairs = [(t[i] + t[i + N//2 - 1], i + 1) for i in range(N//2)]
print(min(p[0] for p in pairs))