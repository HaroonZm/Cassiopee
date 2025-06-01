import sys
from sys import stdin
input = stdin.readline

def main2(args):
    while True:
        n = int(input())
        if n == 0:
            break
        age = [0] * 13
        for _ in range(n):
            a = int(input())
            age[a // 10] += 1
        print(age[0])
        print(age[1])
        print(age[2])
        print(age[3])
        print(age[4])
        print(age[5])
        print(sum(age[6:]))

if __name__ == '__main__':
    main2(sys.argv[1:])