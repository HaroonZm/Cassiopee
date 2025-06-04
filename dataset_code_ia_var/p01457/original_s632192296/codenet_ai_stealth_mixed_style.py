c=0
def f(x): return ['No', 'Yes'][not x]
for _ in range(int(input())):
    data = input().split()
    s = data[1]
    a = int(data[2])
    c = (lambda c, op: c + a if op == '(' else c - a)(c, s)
    print(f(c))
    c = c