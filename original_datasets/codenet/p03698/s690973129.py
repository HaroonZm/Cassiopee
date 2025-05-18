s = input()
d = {}
for i in range(len(s)):
    d[s[i]] = 1
if len(s) == len(d):
    print("yes")
else:
    print("no")