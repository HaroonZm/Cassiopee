import sys

def main():
    for line in sys.stdin:
        n = int(line)
        if n == -1:
            break
        digits = []
        while True:
            digits.append(str(n % 4))
            n //= 4
            if n == 0:
                break
        print(''.join(reversed(digits)))

if __name__ == '__main__':
    main()