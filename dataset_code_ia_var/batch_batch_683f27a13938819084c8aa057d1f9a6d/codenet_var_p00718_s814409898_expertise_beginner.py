import re

def roman_to_arabic(roman):
    values = {'m': 1000, 'c': 100, 'x': 10, 'i': 1}
    total = 0
    temp = ""
    # Split the roman into units like 2c, 3x
    parts = re.findall(r'\d\w', roman)
    leftovers = re.split(r'\d\w', roman)
    # Sometimes, there might be a leading value with only a letter
    if leftovers[0]:
        parts = ['1'+leftovers[0]] + parts
    for part in parts:
        number = int(part[:-1])
        letter = part[-1]
        total += number * values[letter]
    return total

def arabic_to_roman(num):
    letters = ['m', 'c', 'x', 'i']
    divisors = [1000, 100, 10, 1]
    result = ""
    for d, l in zip(divisors, letters):
        count = num // d
        if count > 0:
            result += str(count) + l
        num %= d
    return result

n = int(input())
for _ in range(n):
    s = input().replace(" ", "")
    # Split to get two roman numerals
    split_parts = re.findall(r'[0-9a-z]+', s)
    a = split_parts[0]
    b = split_parts[1]
    val_a = roman_to_arabic(a)
    val_b = roman_to_arabic(b)
    total = val_a + val_b
    result = arabic_to_roman(total)
    # Remove any 0's in the output
    result = result.replace('0', '')
    print(result)