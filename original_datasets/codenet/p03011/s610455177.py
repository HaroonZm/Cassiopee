a = list(map(int, input().split()))
a.remove(max(a))
print(sum(a))