#!/usr/bin/env python3

def main():
    s = input()
    if s.count('x') < 8:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()