n = int(input())
a = [int(i) for i in input().split()]
count = 0
i = 0
while i < n:
    if a[i] % 2 == 0:
        count = count + 1
    i = i + 1
result = 1
j = 0
while j < n:
    result = result * 3
    j = j + 1
sub = 1
k = 0
while k < count:
    sub = sub * 2
    k = k + 1
print(result - sub)