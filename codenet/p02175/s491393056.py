x, a, b = map(int, input().split())
n = int(input())
for i in range(n) :
    s = input()
    if s == 'nobiro' :
        x += a
        if x < 0 :
            x = 0
    elif s == 'tidime' :
        x += b
        if x < 0 :
            x = 0
    else :
        x = 0
print(x)