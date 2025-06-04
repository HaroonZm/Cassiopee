n,m = [int(x) for x in input().split()]
sp = []
for e in input().split():
    sp.append(int(e))
cl = list(map(int, input().split()))
def add(l):
    s = 0
    for i in range(len(l)):
        s = s + l[i]
    return s
somme = add(sp)
ans = sum([somme * a for a in cl])
print(ans)