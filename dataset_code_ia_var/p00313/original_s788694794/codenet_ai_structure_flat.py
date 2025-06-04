n = int(input())
a = list(map(int, input().split()))[1:]
b = list(map(int, input().split()))[1:]
c = list(map(int, input().split()))[1:]
x = 0
y = 0
i = 1
while i <= n:
    cond1 = True
    for val in a:
        if val == i:
            cond1 = False
            break
    if cond1:
        for val in b:
            if val == i:
                cond1 = False
                break
    cond2 = False
    for val in c:
        if val == i:
            cond2 = True
            break
    if cond1 and cond2:
        x = x + 1
    else:
        cond3 = False
        for val in b:
            if val == i:
                cond3 = True
                break
        cond4 = False
        for val in c:
            if val == i:
                cond4 = True
                break
        if cond3 and cond4:
            y = y + 1
    i = i + 1
print(x + y)