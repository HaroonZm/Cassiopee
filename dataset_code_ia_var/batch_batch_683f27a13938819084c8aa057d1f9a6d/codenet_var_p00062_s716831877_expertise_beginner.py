while True:
    try:
        n = input()
    except:
        break
    digits = []
    for char in n:
        digits.append(int(char))
    while len(digits) > 1:
        temp = []
        for i in range(len(digits) - 1):
            num = (digits[i] + digits[i+1]) % 10
            temp.append(num)
        digits = temp
    print(digits[0])