N, m = [int(i) for i in raw_input().split()]

three = list()
for t in range(N):
    three.append(0)

def set_true(c, d):
    cnt = 0
    idx = c
    while idx < d:
        three[idx] = 1
        idx += 1

for loop_var in xrange(m):
    arr = raw_input().split()
    c = int(arr[0])
    d = int(arr[1])
    if c < d:
        set_true(c, d)

res = 1
i = 0
while i < N:
    res += 1
    if three[i]:
        res = res + 2
    i = i + 1
print(res)