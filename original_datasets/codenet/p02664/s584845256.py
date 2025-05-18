t = list(input())

x = len(t)

for i in range(x):
    if t[i] == "?":
        t[i] = "D"
        
for i in t:
    print(i,end = "")