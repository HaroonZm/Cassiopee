N = int(input())
S = input()
a = 0
b = 0
for s in S:
    if s == '(':
        a += 1
    else:
        if a > 0:
            a -= 1
        else:
            b += 1
ans = '(' * b + S + ')' * a
print(ans)