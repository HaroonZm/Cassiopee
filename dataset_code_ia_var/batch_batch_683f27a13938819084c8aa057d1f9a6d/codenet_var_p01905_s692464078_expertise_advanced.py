from operator import sub
from sys import stdin

def main():
    N, M = map(int, stdin.readline().split())
    print(sub(sub(N, M), 1))

if __name__ == '__main__':
    main()