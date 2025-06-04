while True:
    m, n = map(int, input().split())
    if m == 0:
        break
    m **= n
    s = ""
    d = 68
    ls = [
        'Man', 'Oku', 'Cho', 'Kei', 'Gai', 'Jo', 'Jou', 'Ko',
        'Kan', 'Sei', 'Sai', 'Gok', 'Ggs', 'Asg', 'Nyt', 'Fks', 'Mts'
    ][::-1]
    while d:
        if int(m // 10 ** d) >= 1:
            s += str(int(m // 10 ** d)) + ls[int((d - 4) // 4)]
            m %= 10 ** d
        d -= 4
    if m:
        s += str(m)
    print(s)