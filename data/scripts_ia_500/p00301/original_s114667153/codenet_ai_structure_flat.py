w = int(input())
res = ''
while w > 0:
    r = w % 3
    if r == 0:
        res += '0'
        w //= 3
    elif r == 1:
        res += '+'
        w //= 3
    else:
        res += '-'
        w += 1
        w //= 3
print(res[::-1])