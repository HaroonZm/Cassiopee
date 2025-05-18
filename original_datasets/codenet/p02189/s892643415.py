N = int(input())
a = [int(x) for x in input().split()]

print(a.index(min(a)) + 1)