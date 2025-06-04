n,q = [int(x) for x in input().split()]
s = input()
count = 0
c = []
for k in range(n):
    if k == 0:
        c.append(0)
    else:
        if s[k-1] == 'A':
            if s[k] == 'C':
                count = count + 1
        c.append(count)

for __ in range(q):
    tokens = input().split()
    l = int(tokens[0])
    r = int(tokens[1])
    res = c[r-1] - c[l-1]
    print(res)