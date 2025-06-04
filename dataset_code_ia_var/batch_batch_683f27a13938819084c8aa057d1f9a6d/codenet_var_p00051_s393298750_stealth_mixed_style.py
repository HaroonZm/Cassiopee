m = int(input())
for _ in range(m):
    s = input()
    lst = list(s)
    lst.sort()
    t = ''.join(lst)
    u = t[::-1]
    print(eval(u) - int(t))