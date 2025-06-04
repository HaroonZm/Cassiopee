n = int(input())
while n > 0:
    m = 1000 - n
    a = int(m // 500)
    b = int((m % 500) // 100)
    c = int((m % 100) // 50)
    d = int((m % 50) // 10)
    e = int((m % 10) // 5)
    f = int((m % 5) // 1)
    print(a + b + c + d + e + f)
    n = int(input())