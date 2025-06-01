n = int(input())
while n > 0:
    m = 1000 - n
    a = m // 500
    b = (m % 500) // 100
    c = (m % 100) // 50
    d = (m % 50) // 10
    e = (m % 10) // 5
    f = m % 5
    somme = 0
    for piece in [a, b, c, d, e, f]:
        somme += piece
    print(somme)
    n = int(input())