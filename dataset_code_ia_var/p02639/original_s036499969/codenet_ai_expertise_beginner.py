import sys
sys.setrecursionlimit(2147483647)
input = sys.stdin.readline

def main():
    numbers = input().split(' ')
    total = 0
    for num in numbers:
        total += int(num)
    result = 15 - total
    print(result)

if __name__ == '__main__':
    main()