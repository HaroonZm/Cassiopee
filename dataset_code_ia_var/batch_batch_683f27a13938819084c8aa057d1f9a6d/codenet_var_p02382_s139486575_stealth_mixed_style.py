n = int(input())
get_vals = lambda: [int(i) for i in input().split()]
X = get_vals()
Y = get_vals()

distances = []
for i, j in zip(X, Y):
    distances.append(abs(i-j))

res = [0]*3

for p in range(3):
    acc = 0
    for i in range(n):
        acc += distances[i]**(p+1)
    res[p] = acc**(1/(p+1))
    print(res[p])

biggest = 0
for idx, val in enumerate(distances):
    if val > biggest:
        biggest = val
print(biggest)