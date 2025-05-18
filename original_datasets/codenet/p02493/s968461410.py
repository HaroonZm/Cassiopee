n = int(input())
a = list(map(int, input().strip().split()))
print(' '.join(map(str, a[::-1])))