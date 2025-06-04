while True:
    input_tokens = list(map(str, input().split()))
    input_command = input_tokens[0]
    input_value1 = int(input_tokens[1])
    input_value2 = int(input_tokens[2])
    if input_command == "#":
        break
    if input_value1 <= 30:
        print(" ".join(input_tokens))
    elif input_value1 == 31 and input_value2 <= 4:
        print(" ".join(input_tokens))
    else:
        input_tokens[0] = "?"
        updated_value1 = input_value1 - 30
        input_tokens[1] = str(updated_value1)
        print(" ".join(input_tokens))