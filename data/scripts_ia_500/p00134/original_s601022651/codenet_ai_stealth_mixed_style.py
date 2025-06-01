n = int(input())
def f():
    s = 0
    for i in range(n):
        s += int(raw_input())
    return s
print f() / float(n)