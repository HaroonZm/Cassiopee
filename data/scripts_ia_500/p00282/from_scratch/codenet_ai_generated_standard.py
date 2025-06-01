units = ["", "Man", "Oku", "Cho", "Gai", "Jo", "Ko", "Kan", "Sei", "Sai"]
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    num = pow(m, n)
    parts = []
    while num > 0:
        parts.append(num % 10000)
        num //= 10000
    res = []
    for i in range(len(parts)-1,-1,-1):
        if parts[i] != 0:
            res.append(str(parts[i]) + units[i])
    print(''.join(res) if res else "0")