n = int(input())

def check(x):
    for i in range(1,10):
        for j in range(1,10):
            if i*j==x: return True
    return False

class R:
    pass

r = R()
setattr(r, 'ans', 'No')
if check(n):
    r.ans = 'Yes'

print(getattr(r, 'ans'))