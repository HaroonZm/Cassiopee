us = ["", "Man", "Oku", "Cho", "Kei", "Gai", "Jo", "Jou", "Ko", "Kan", "Sei", "Sai", "Gok", "Ggs", "Asg", "Nyt", "Fks", "Mts"]

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    val = pow(m, n)
    if val < 10_000:
        print(val)
        continue

    s = f"{val:0>{((val.bit_length() + 13) // 14) * 4}}"
    groups = [int(s[i:i+4]) for i in range(0, len(s), 4)]

    result = ''.join(f"{x}{us[len(groups) - i - 1]}" for i, x in enumerate(groups) if x)
    print(result)