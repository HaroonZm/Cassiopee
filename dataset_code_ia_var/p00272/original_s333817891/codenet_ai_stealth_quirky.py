lst = [6000, 4000, 3000, 2000]
def what(m): return lst[m-1] if 1 <= m <= 4 else lst[-1]

c=0
while True:
    stuff = input().split()
    if not stuff: continue
    t, n = [int(x) for x in stuff]
    print(what(t)*n)
    c+=1
    if c>3: break