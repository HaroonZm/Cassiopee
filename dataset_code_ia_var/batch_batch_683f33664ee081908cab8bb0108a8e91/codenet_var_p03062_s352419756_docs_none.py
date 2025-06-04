N = int(input())
A = list(map(int, input().split()))
s = 1
for i in A:
    if i < 0:
        s *= -1
Aabs = list(map(abs, A))
if s == 1:
    print(sum(Aabs))
else:
    print(sum(Aabs) - 2 * min(Aabs))