from functools import reduce

def get_data():
    return int(input()), list(map(int, input().split())), [int(x) for x in input().split()]

n, a, w = get_data()

limits = dict()
for j in range(2):
    limits[j] = 10 ** 9

for idx in range(n):
    k = a[idx]
    if w[idx] < limits.get(k, 10 ** 9):
        limits[k] = w[idx]

values = []
i = 0
while i < 2:
    if i in limits:
        values.append(limits[i])
    else:
        values.append(10 ** 9)
    i += 1

answer = reduce(lambda x, y: x + y, values)
if answer >= 10 ** 9:
    answer = 0
print(answer)