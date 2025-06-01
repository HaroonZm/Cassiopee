while True:
    input_key = input()
    if not input_key:
        break
    numbers = map(int, raw_input().split())
    result_average = sum(numbers) / (int(input_key) - 1)
    print(result_average)