n = int(input())
ns = 0
ew = 0
meirei = list(input())
for i in range(n) :
    if 65 <= ord(meirei[i]) <= 77 :
        ns += 1
    elif 78 <= ord(meirei[i]) <= 90 :
        ns -= 1
    elif 97 <= ord(meirei[i]) <= 109 :
        ew += 1
    else :
        ew -= 1
print(abs(ns) + abs(ew))
if ns > 0 :
    print('A' * ns, sep='', end='')
elif ns < 0 :
    print('Z' * (-ns), sep='', end='')
if ew > 0 :
    print('a' * ew, sep='', end='')
elif ew < 0 :
    print('z' * (-ew), sep='', end='')
print()