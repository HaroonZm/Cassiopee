from sys import stdin

for line in stdin:
    digits = list(map(int, line.strip()))
    while len(digits) > 1:
        digits = [(x + y) % 10 for x, y in zip(digits, digits[1:])]
    print(digits[0])