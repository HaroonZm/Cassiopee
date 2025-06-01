s1 = list(range(11)) + [10]*3
def f(x):
    if x == []:
        return [0]
    e = s1[x[0]]
    A1 = [e + e1 for e1 in f(x[1:])]
    A2 = []
    if e == 1:
        A2 = [e + 10 for e in A1]
    return list(filter(lambda x: x < 22, A1 + A2))

while True:
    x = list(map(int, input().split()))
    if x[0] == 0:
        break
    a = f(x)
    print(max(a) if a else 0)