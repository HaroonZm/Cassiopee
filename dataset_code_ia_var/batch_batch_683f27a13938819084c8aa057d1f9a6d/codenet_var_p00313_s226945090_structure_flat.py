n = int(input())
a = list(map(int, input().split()))
X = a.pop(0)
a = set(a)
b = list(map(int, input().split()))
Y = b.pop(0)
b = set(b)
c = list(map(int, input().split()))
Z = c.pop(0)
c = set(c)
a_bar = set()
for x in range(1, n+1):
    if x not in a:
        a_bar.add(x)
temp1 = set()
for x in a_bar:
    if x in c:
        temp1.add(x)
temp2 = set()
for x in b:
    if x in c:
        temp2.add(x)
ans = temp1
for x in temp2:
    ans.add(x)
print(len(ans))