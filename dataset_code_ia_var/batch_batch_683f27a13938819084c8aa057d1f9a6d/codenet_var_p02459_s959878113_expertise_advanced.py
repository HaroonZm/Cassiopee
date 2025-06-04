import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    q = int(input())
    dictionary = {}
    for _ in range(q):
        op, key, *value = input().split()
        if op == '0':
            dictionary[key] = int(value[0])
        else:
            print(dictionary[key])

if __name__ == "__main__":
    main()