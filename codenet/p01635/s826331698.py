n, t = map(int, input().split())
F = list(input())

total = 0
while F != []:
    tmp = F.pop(0)
    if F == []:
        total += n
    elif tmp == "n":
        p = F.pop(0)
        if p == "^":
            num = F.pop(0)
            total += pow(n, int(num))
        else:
            total += n

time = total * t
if time > 1000000000:
    print("TLE")
else:
    print(time)