x = input()
n = int(input())
ans = 0
i = 0
while i < n:
    y = list(input())
    j = 0
    while j < len(x) - 1:
        y.append(y[j])
        j += 1
    y_str = ""
    k = 0
    while k < len(y):
        y_str += y[k]
        k += 1
    occ = False
    m = 0
    while m <= len(y_str) - len(x):
        if y_str[m:m+len(x)] == x:
            occ = True
            break
        m += 1
    if occ:
        ans += 1
    i += 1
print(ans)