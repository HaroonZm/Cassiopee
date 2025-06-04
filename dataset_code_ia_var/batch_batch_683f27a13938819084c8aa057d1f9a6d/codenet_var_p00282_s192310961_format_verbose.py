while True:

    base, exponent = map(int, input().split())

    if base + exponent == 0:
        break

    power_result = base ** exponent

    if power_result < 10000:
        print(power_result)
        continue

    power_as_str = str(power_result)

    while len(power_as_str) % 4 > 0:
        power_as_str = "0" + power_as_str

    japanese_large_units = [
        "",
        "Man",
        "Oku",
        "Cho",
        "Kei",
        "Gai",
        "Jo",
        "Jou",
        "Ko",
        "Kan",
        "Sei",
        "Sai",
        "Gok",
        "Ggs",
        "Asg",
        "Nyt",
        "Fks",
        "Mts"
    ]

    group_length = 4
    total_length = len(power_as_str)

    for group_start_index in range(0, total_length, group_length):
        digit_group = int(power_as_str[group_start_index:group_start_index + group_length])

        if digit_group == 0:
            continue

        unit_index = (total_length - group_start_index) // group_length - 1

        print(str(digit_group) + japanese_large_units[unit_index], end="")

    print()