answer = int(input())  # starting number, let's go
while True:
    operation = input()  # expecting +, -, *, / or =
    if operation == '+':
        val = int(input())
        answer += val  # just adding here
    elif operation == '-':
        val = int(input())
        answer -= val  # subtraction time
    elif operation == '*':
        val = int(input())
        answer *= val  # multiplication
    elif operation == '/':
        val = int(input())
        # integer division, watch out for zero though
        answer //= val
    elif operation == '=':
        print(answer)
        break  # done, exiting loop
    # no else: handling wrong input here, should add one maybe?