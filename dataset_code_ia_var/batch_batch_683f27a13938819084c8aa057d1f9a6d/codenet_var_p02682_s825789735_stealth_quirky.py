get = lambda: [int(i) for i in __import__('sys').stdin.readline().split()]
(a,b,c,k) = get()
x = k
if k > a:
    if k <= a+b:
        x = a
    elif k <= a+b+c:
        x = a - (k - (a+b))
print([x, k][k <= a])