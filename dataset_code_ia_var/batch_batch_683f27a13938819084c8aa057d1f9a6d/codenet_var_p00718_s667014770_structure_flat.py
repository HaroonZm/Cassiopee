import re

PATTERN = re.compile(r"[2-9]*[mcxi]")
NUMBERS = "23456789"
TABLE = {"m": 1000, "c": 100, "x": 10, "i": 1}

n = int(input())
for _ in range(n):
    mcxi1, mcxi2 = input().split()
    answer1 = 0
    for segment in re.findall(PATTERN, mcxi1):
        if segment[0] in NUMBERS:
            answer1 += int(segment[0]) * TABLE[segment[-1]]
        else:
            answer1 += TABLE[segment[-1]]
    answer2 = 0
    for segment in re.findall(PATTERN, mcxi2):
        if segment[0] in NUMBERS:
            answer2 += int(segment[0]) * TABLE[segment[-1]]
        else:
            answer2 += TABLE[segment[-1]]
    number = answer1 + answer2
    m, cxi = divmod(number, 1000)
    c, xi = divmod(cxi, 100)
    x, i = divmod(xi, 10)
    result = ""
    if m == 1:
        result += "m"
    elif m > 1:
        result += str(m) + "m"
    if c == 1:
        result += "c"
    elif c > 1:
        result += str(c) + "c"
    if x == 1:
        result += "x"
    elif x > 1:
        result += str(x) + "x"
    if i == 1:
        result += "i"
    elif i > 1:
        result += str(i) + "i"
    print(result)