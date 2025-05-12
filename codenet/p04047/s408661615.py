N = int(input())
Ls = list(map(int, input().split()))

Ls.sort()

print(sum(Ls[::2]))