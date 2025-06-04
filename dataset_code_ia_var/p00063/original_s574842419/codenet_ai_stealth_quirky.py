s = [0]
def f():
    while 41:
        try:
            j = input()
            (lambda x: s.__setitem__(0, s[0]+1) if x == x[::-1] else None)(j)
        except:
            return
f()
print(s[-1])