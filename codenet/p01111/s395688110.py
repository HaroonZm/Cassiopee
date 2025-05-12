import math
def main(n):
    for i in range(int((1 + math.sqrt(1 + 8 * n)) // 2) + 1, 0, -1):
        if float.is_integer(n / i - (i - 1) / 2) and n / i - (i - 1) / 2 > 0:
            print(int(n / i - (i - 1) / 2), i)
            return

while 1:
    n = int(input())
    if n == 0:
        break
    main(n)