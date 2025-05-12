#!/usr/bin/env python

def main():
    n = raw_input()
    numbers = [int(x) for x in raw_input().split(" ")]
    numbers.sort()
    print " ".join([str(number) for number in numbers])

if __name__ == '__main__':
    main()