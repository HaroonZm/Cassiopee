while True:
    input_tokens = list(map(str, input().split()))
    command = input_tokens[0]
    value_a = int(input_tokens[1])
    value_b = int(input_tokens[2])
    if command == "#":
        break
    if (value_a == 31 and value_b >= 5) or (value_a >= 32):
        input_tokens[0] = "?"
        input_tokens[1] = str(value_a - 30)
    print(' '.join(map(str, input_tokens)))