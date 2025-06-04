import sys

a, b = 0, 600

if __name__ == '__main__':
    for line in sys.stdin:
        d = int(line)
        sum = 0
        i = a
        while i < b:
            sum += d * (i ** 2)
            i += d
        print(sum)