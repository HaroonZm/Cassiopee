d, n = map(int, input().split())
t = []
i = 0
while i < d:
    t.append(int(input()))
    i += 1

abc = []
i = 0
while i < n:
    abc.append(list(map(int, input().split())))
    i += 1

memo = [-1]*101

t_list = []
i = 0
while i < 61:
    t_list.append(set())
    i += 1

i = 0
while i < n:
    a, b, c = abc[i]
    j = a
    while j <= b:
        t_list[j].add(c)
        j += 1
    i += 1

for x in t_list[t[0]]:
    memo[x] = 0

i = 1
while i < d:
    memo2 = [-1]*101
    temp = []
    for v in t_list[t[i]]:
        temp.append(v)
    j = 0
    while j < 101:
        if memo[j] != -1:
            k = 0
            while k < len(temp):
                l = temp[k]
                memo2[l] = max(memo2[l], memo[j]+abs(j-l))
                k += 1
        j += 1
    memo = memo2
    i += 1

res = -1
i = 0
while i < 101:
    if memo[i] > res:
        res = memo[i]
    i += 1
print(res)