import re

def mcxi2int(mcxi_str):
    total = 0
    numbers = "23456789"
    table = {"m": 1000, "c": 100, "x": 10, "i": 1}
    pattern = r"[2-9]*[mcxi]"
    parts = re.findall(pattern, mcxi_str)
    for part in parts:
        if len(part) == 1:
            num = 1
            letter = part[0]
        else:
            num = int(part[0])
            letter = part[1]
        total += num * table[letter]
    return total

def int2mcxi(number):
    m = number // 1000
    rest = number % 1000
    c = rest // 100
    rest = rest % 100
    x = rest // 10
    i = rest % 10
    result = ""
    if m > 0:
        if m == 1:
            result += "m"
        else:
            result += str(m) + "m"
    if c > 0:
        if c == 1:
            result += "c"
        else:
            result += str(c) + "c"
    if x > 0:
        if x == 1:
            result += "x"
        else:
            result += str(x) + "x"
    if i > 0:
        if i == 1:
            result += "i"
        else:
            result += str(i) + "i"
    return result

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        mcxi1, mcxi2 = input().split()
        num1 = mcxi2int(mcxi1)
        num2 = mcxi2int(mcxi2)
        total = num1 + num2
        print(int2mcxi(total))