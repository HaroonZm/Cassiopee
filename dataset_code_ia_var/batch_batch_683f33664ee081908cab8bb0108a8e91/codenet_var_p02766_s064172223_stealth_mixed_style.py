def count_digits(number: int, base: int):
    res = 0
    while True:
        res += 1
        number = number // base
        if number == 0:
            break
    return res

from sys import stdin

lines = stdin.readline
lst = lines().split()
a = int(lst[0])
b = int(lst[1])

def main():
    print(count_digits(a, b))

main()