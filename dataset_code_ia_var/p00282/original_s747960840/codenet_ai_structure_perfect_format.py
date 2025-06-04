unit = [
    "", "Man", "Oku", "Cho", "Kei", "Gai", "Jo", "Jou", "Ko",
    "Kan", "Sei", "Sai", "Gok", "Ggs", "Asg", "Nyt", "Fks", "Mts"
]
while 1:
    m, n = map(int, raw_input().split())
    if m == 0:
        break
    a = m ** n
    ans = ""
    for i in xrange(20):
        c = a % 10000
        if c > 0:
            ans = str(c) + unit[i] + ans
        a //= 10000
        if a == 0:
            break
    print ans