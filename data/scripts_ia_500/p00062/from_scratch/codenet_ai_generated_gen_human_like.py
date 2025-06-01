while True:
    line = input().strip()
    if not line:
        break
    numbers = list(map(int, line))
    while len(numbers) > 1:
        numbers = [(numbers[i] + numbers[i+1]) % 10 for i in range(len(numbers)-1)]
    print(numbers[0])