def is_multiple_of_11(s):
    # Check if the string s represents a multiple of 11
    n = int(s)
    return n % 11 == 0

while True:
    number = input()
    if number == '0':
        break
    count = 0
    length = len(number)
    for start in range(length):
        if number[start] == '0':
            continue
        for end in range(start + 1, length + 1):
            substring = number[start:end]
            if is_multiple_of_11(substring):
                count += 1
    print(count)