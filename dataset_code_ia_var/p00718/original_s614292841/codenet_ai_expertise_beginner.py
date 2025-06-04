ans_list = []
n = int(input())

# m = 1000, c = 100, x = 10, i = 1
symbols = ['i', 'x', 'c', 'm']

def value(s):
    total = 0
    for idx in range(4):
        ch = symbols[idx]
        pos = s.find(ch)
        if pos != -1:
            if pos == 0 or s[pos - 1] in symbols:
                total += 10**idx
            else:
                total += int(s[pos - 1]) * 10**idx
    return total

def mcxi(num):
    res = ""
    for idx in range(3,-1,-1):
        digit = num // (10**idx)
        if digit >= 1:
            if digit == 1:
                res += symbols[idx]
            else:
                res += str(digit) + symbols[idx]
        num %= 10**idx
    return res

for i in range(n):
    a, b = input().split()
    sum_val = value(a) + value(b)
    ans = mcxi(sum_val)
    ans_list.append(ans)

for a in ans_list:
    print(a)