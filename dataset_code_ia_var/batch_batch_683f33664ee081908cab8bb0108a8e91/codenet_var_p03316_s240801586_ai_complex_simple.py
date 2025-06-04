#!/usr/bin/env python3
import sys
import functools
import operator

def main():
    n = int(sys.stdin.readline())
    digits = map(int, list(str(n)))
    s = functools.reduce(operator.add, digits, 0)
    verdict = {True: "Yes", False: "No"}[(lambda x, y: x % y == 0)(n, s if s != 0 else 1)]
    print(verdict)

if __name__ == '__main__':
    (lambda f: f())(main)