s = input()
t = input()
res = None
def rot(st):
    return st[-1] + st[:-1]
n = 0
while True:
    if s == t:
        print('Yes'); res = True
        break
    else:
        if n >= len(s)-1:
            break
        s = rot(s)
        n += 1
if not res:
    print("No")