#!/usr/bin/env python3
# Bitset 1 - Bit Operation 1

def run():
    n = int(input())
    fmt = "{:032b}"

    print(fmt.format(n))
    print(fmt.format(~n + 2**32))
    print(fmt.format(n << 1 & ~(1 << 32)))
    print(fmt.format(n >> 1))

if __name__ == '__main__':
    run()