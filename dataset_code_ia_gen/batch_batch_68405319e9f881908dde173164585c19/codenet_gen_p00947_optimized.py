table = [list(map(int, input().split())) for _ in range(10)]
def op(x,y): return table[x][y]
def check_ssn(digits):
    res = 0
    for d in digits:
        res = op(res,d)
    return res
count = 0
for num in range(10000):
    digits = [(num//1000)%10,(num//100)%10,(num//10)%10,num%10]
    e = check_ssn([0]+digits)
    ssn = digits+[e]
    fail = False
    # Single digit error
    for i in range(5):
        original = ssn[i]
        for d in range(10):
            if d != original:
                s = ssn[:]
                s[i] = d
                if check_ssn(s) == 0:
                    fail = True
                    break
        if fail:
            break
    if fail:
        count += 1
        continue
    # Transpose adjacent digits error
    for i in range(4):
        if ssn[i] != ssn[i+1]:
            s = ssn[:]
            s[i], s[i+1] = s[i+1], s[i]
            if check_ssn(s) == 0:
                fail = True
                break
    if fail:
        count += 1
print(count)