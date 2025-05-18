s = input()
c1,c2 = 0,0
for i in range(len(s)):
    if i%2 and s[i] == "1":
        c1 += 1
    elif i%2 and s[i] == "0":
        c2 += 1
    elif i%2==0 and s[i] == "0":
        c1 += 1
    else:
        c2 += 1
print(min(c1,c2))