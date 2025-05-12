#!/usr/bin/env python3

import re

PATTERN = re.compile(r"[2-9]*[mcxi]")
NUMBERS = "23456789"
TABLE = {"m": 1000, "c": 100, "x": 10, "i": 1}

def mcxi2int(mcxi_str):
    answer = 0
    for segment in re.findall(PATTERN, mcxi_str):
        answer += TABLE[segment[-1]] * \
            (int(segment[0]) if segment[0] in NUMBERS else 1)
    return answer

def int2mcxi(number):
    mcxi_prefixes = dict()
    mcxi_prefixes["m"], cxi = divmod(number, 1000)
    mcxi_prefixes["c"], xi = divmod(cxi, 100)
    mcxi_prefixes["x"], mcxi_prefixes["i"] = divmod(xi, 10)
    result = ""
    for char in "mcxi":
        if mcxi_prefixes[char] == 1:
            result += char
        elif mcxi_prefixes[char] > 1:
            result += str(mcxi_prefixes[char]) + char
    return result

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        mcxi1, mcxi2 = input().split()
        print(int2mcxi(mcxi2int(mcxi1) + mcxi2int(mcxi2)))