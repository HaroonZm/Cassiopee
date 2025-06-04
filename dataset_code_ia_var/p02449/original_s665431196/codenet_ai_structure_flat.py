import itertools
n = int(input())
a = [int(i) for i in input().split(" ")]
perms = list(itertools.permutations([i+1 for i in range(n)]))
i = 0
while i < len(perms):
    if list(perms[i]) == a:
        break
    i += 1
if i > 0:
    s = ""
    j = 0
    while j < n:
        s += str(perms[i-1][j])
        if j < n-1:
            s += " "
        j += 1
    print(s)
s = ""
j = 0
while j < n:
    s += str(perms[i][j])
    if j < n-1:
        s += " "
    j += 1
print(s)
if i+1 < len(perms):
    s = ""
    j = 0
    while j < n:
        s += str(perms[i+1][j])
        if j < n-1:
            s += " "
        j += 1
    print(s)