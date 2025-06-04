input_hour, input_offset = map(int, input().split())
result_hour = (input_hour + input_offset) % 24
print(result_hour)