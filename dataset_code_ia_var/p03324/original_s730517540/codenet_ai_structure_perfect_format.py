import sys

def solve(a, b):
    if a == 0 and b <= 99:
        return b
    elif a == 1 and b <= 99:
        return 100 * b
    elif a == 2 and b <= 99:
        return 10000 * b
    elif a == 0:
        return 101
    elif a == 1:
        return 10100
    else:
        return 1010000

def readQuestion():
    line = sys.stdin.readline().rstrip()
    str_a, str_b = line.split(' ')
    return int(str_a), int(str_b)

def main():
    a, b = readQuestion()
    answer = solve(a, b)
    print(answer)

if __name__ == '__main__':
    main()