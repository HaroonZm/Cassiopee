n = int(input())
s = set()
for _ in range(n):
    name = input()
    s.add(name)

k = False

m = int(input())
t = []
for _ in range(m):
    item = input()
    t.append(item)

for i in t:
    if i in s:
        k = not k
        if k == True:
            print("Opened by", i)
        else:
            print("Closed by", i)
    else:
        print("Unknown", i)