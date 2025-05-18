N = int(input())
P = input().split()
if P[0]=="T" and P[1]=="F":
    out = "F"
else:
    out = "T"
for i in range(N-2):
    if out == "T" and P[i+2] == "F":
        out = "F"
    else:
        out = "T"
print(out)