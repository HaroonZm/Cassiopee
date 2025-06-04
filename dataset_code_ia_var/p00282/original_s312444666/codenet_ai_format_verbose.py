while True:

    base_number, exponent = map(int, input().split())

    if base_number == 0:
        break

    power_result = base_number ** exponent

    output_string = ""

    current_exponent = 68

    japanese_units = [
        'Mts', 'Fks', 'Nyt', 'Asg', 'Ggs', 'Gok', 'Sai', 'Sei',
        'Kan', 'Ko', 'Jou', 'Jo', 'Gai', 'Kei', 'Cho', 'Oku', 'Man'
    ][::-1]

    while current_exponent:

        divisor = 10 ** current_exponent

        if int(power_result / divisor) >= 1:
            output_string += (
                str(int(power_result / divisor))
                + japanese_units[int((current_exponent - 4) / 4)]
            )
            power_result = power_result % divisor

        current_exponent -= 4

    if power_result:
        output_string += str(power_result)

    print(output_string)