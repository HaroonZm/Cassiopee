total_seconds_input = int(input())

number_of_hours = total_seconds_input // 3600

remaining_seconds_after_hours = total_seconds_input % 3600

number_of_minutes = remaining_seconds_after_hours // 60

number_of_seconds = remaining_seconds_after_hours % 60

print(number_of_hours, number_of_minutes, number_of_seconds, sep=":")