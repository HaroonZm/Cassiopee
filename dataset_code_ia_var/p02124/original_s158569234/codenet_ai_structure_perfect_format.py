x = int(input())
n = x / 100

def f(n):
    if n == 0:
        return 'ai1333'
    else:
        a = f(n - 1)
        b = a + '3'
        return b

print(f(n))