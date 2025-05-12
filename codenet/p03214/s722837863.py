N = int(input())
Na = list(map(int, input().split()))
mean = sum(Na)/N
print(min((abs(a-mean),i)  for i, a in enumerate(Na))[1])