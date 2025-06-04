units_list = [
    "", "Man", "Oku", "Cho", "Kei", "Gai", "Jo", "Jou", "Ko",
    "Kan", "Sei", "Sai", "Gok", "Ggs", "Asg", "Nyt", "Fks", "Mts"
]

while True:

    user_input = raw_input()

    base_number, exponent = map(int, user_input.split())

    if base_number == 0:
        break

    power_result = base_number ** exponent

    formatted_result = ""

    for unit_index in xrange(20):

        current_chunk = power_result % 10000

        if current_chunk > 0:
            formatted_result = str(current_chunk) + units_list[unit_index] + formatted_result

        power_result /= 10000

        if power_result == 0:
            break

    print formatted_result