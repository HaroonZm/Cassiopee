unit = ["", "Man", "Oku", "Cho", "Kei", "Gai", "Jo", "Jou", "Ko",
        "Kan", "Sei", "Sai", "Gok", "Ggs", "Asg", "Nyt", "Fks", "Mts"]

while True:
    m, n = map(int, input().split())
    if m == 0:
        break
    a = pow(m, n)
    parts = [(a // 10_000**i) % 10_000 for i in range(20)]
    ans = ''.join(f"{part}{unit[i]}" for i, part in enumerate(parts) if part)[::-1]
    print(ans[::-1])