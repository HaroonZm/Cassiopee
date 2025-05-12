w = int(input())
res = ''
while w > 0:
    if w%3 == 0:
        res += '0'
    elif w%3 == 1:
        res += '+'
    else:
        res += '-';
        w += 1
    w //= 3
print( res[::-1] )