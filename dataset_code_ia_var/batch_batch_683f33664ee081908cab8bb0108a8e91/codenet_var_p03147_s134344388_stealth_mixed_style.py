n = int(input())
h = list(map(int, input().split()))
kadan = [0] * n
c = 0
done = [False] * n

def all_true(flags):
    for f in flags:
        if not f:
            return False
    return True

i = 1
while True:
    c += 1
    flag = False
    x = 0
    while x < n:
        if not done[x]:
            flag = True
            if kadan[x] == h[x]:
                done[x] = True
            else:
                kadan[x] += 1
        elif done[x] == True and flag == False:
            pass
        else:
            break
        x += 1
    if not (False in done):
        break
    i += 1
else:
    pass

print(c - 1)