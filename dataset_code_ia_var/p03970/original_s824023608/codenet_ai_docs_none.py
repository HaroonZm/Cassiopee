s = input()
c = "CODEFESTIVAL2016"
a = 0
for i in range(len(c)):
    if s[i] != c[i]:
        a += 1
print(a)