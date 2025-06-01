a = list(map(int, input().split()))
b = list(map(int, input().split()))
s, t = sum(a), sum(b)
print(s if s >= t else t)