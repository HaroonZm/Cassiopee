s = input()
def f(st):
    r = [st[0]]
    i = 1
    while i < len(st):
        if st[i] != st[i-1]:
            r.append(st[i])
        i += 1
    return r

class X: pass

res = (lambda x: len(x)-1)(f(s)) if s else 0
setattr(X, 'a', res)
print(getattr(X, 'a'))