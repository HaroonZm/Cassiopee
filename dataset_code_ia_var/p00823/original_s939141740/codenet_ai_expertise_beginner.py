dic = {}

while True:
    s = input()
    if s == 'END_OF_FIRST_PART':
        break
    a, b = s.split()
    dic[a] = b

def pre():
    global s
    s = list(s)
    i = 1
    while i < len(s):
        if s[i].isdigit():
            s.insert(i, '*')
            i += 1
            while i+1 < len(s) and s[i+1].isdigit():
                i += 1
        elif (s[i] == '(' or s[i].isupper()) and s[i-1] != '(':
            s.insert(i, '+')
            i += 1
        i += 1
    s = ''.join(s)

def mole():
    global p, s
    num = term()
    while p < len(s):
        if s[p] == '+':
            p += 1
            num += term()
        else:
            break
    return num

def term():
    global p, s
    num = factor()
    while p < len(s):
        if s[p] == '*':
            p += 1
            num *= factor()
        else:
            break
    return num

def factor():
    global p, s
    if p < len(s) and s[p] == '(':
        p += 1
        num = mole()
        p += 1
        return num
    else:
        return number()

def number():
    global p, s, f
    num = 0
    if s[p].isdigit():
        while p < len(s) and s[p].isdigit():
            num = num * 10 + int(s[p])
            p += 1
    elif s[p] != '(' and s[p] != ')':
        temp = ''
        while p < len(s) and s[p] not in '()+*':
            temp += s[p]
            p += 1
        if temp in dic:
            num = int(dic[temp])
        else:
            f = False
    return num

while True:
    s = input()
    if s == '0':
        break
    p = 0
    f = True
    pre()
    ans = mole()
    if f:
        print(ans)
    else:
        print('UNKNOWN')