from functools import reduce

while (number := input()) != "0":
    print(reduce(lambda acc, digit: acc + int(digit), number, 0))