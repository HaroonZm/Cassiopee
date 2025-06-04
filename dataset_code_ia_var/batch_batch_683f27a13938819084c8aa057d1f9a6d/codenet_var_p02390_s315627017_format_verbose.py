total_seconds_input = int(input())

number_of_hours = int(total_seconds_input // (60 ** 2))

remaining_seconds_after_hours = int(total_seconds_input % (60 ** 2))

number_of_minutes = int(remaining_seconds_after_hours // 60)

number_of_seconds = int(remaining_seconds_after_hours % 60)

print("{}:{}:{}".format(number_of_hours, number_of_minutes, number_of_seconds))