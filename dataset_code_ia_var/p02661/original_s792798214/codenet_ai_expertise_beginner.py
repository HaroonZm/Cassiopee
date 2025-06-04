n = int(input())
a = []
b = []
for i in range(n):
    values = input().split()
    a.append(int(values[0]))
    b.append(int(values[1]))

a.sort()
b.sort()

def find_median(lst):
    length = len(lst)
    if length % 2 == 1:
        return lst[length // 2]
    else:
        return (lst[length // 2] + lst[length // 2 - 1]) / 2

median_a = find_median(a)
median_b = find_median(b)

if n % 2 == 1:
    result = abs(median_b - median_a) + 1
else:
    result = int(abs(median_b - median_a) * 2) + 1

print(int(result))