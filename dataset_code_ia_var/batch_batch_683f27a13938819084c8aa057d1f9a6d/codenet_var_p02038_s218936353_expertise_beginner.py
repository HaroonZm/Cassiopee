N = int(input())
P = input().split()
if P[0] == "T" and P[1] == "F":
    res = "F"
else:
    res = "T"
i = 2
while i < N:
    if res == "T" and P[i] == "F":
        res = "F"
    else:
        res = "T"
    i = i + 1
print(res)