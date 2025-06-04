n = int(input())
s = input().split()
a = set()
for x in s:
    a.add(str(x))
if len(a) >= 4:
    print("Four")
else:
    print("Three")