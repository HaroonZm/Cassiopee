number = input()

while number != "0":
    total = 0
    for digit in number:
        total = total + int(digit)
    print(total)
    number = input()