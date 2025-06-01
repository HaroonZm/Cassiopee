d,n=tuple(map(int,input().split()))
t=[]
for _ in range(d):
    t.append(int(input()))
abc=[]
for _ in range(n):
    line = input()
    parts = line.split()
    abc.append([int(x) for x in parts])

memo = [-1 for _ in range(101)]
t_list = [set() for _ in range(61)]

for triple in abc:
    a,b,c = triple[0], triple[1], triple[2]
    j = a
    while j <= b:
        t_list[j].add(c)
        j += 1

for elem in t_list[t[0]]:
    memo[elem] = 0

for i in t[1:]:
    memo2 = [-1 for _ in range(101)]
    temp = list(t_list[i])
    for idx, val in enumerate(memo):
        if val != -1:
            for l in temp:
                memo2[l] = max(memo2[l], val + abs(idx - l))
    memo = memo2

print(max(memo))