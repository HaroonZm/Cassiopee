def J(string):
    return string[-1] + string[:-1] if len(string) >= 2 else string

def C(string):
    return string[1:] + string[0] if len(string) >= 2 else string

def E(string):
    if len(string) == 1:
        return string
    if len(string) % 2:
        return string[len(string) // 2 + 1:] + string[len(string) // 2] + string[0:len(string) // 2]
    else:
        return string[len(string) // 2:] + string[0:len(string) // 2]

def A(string):
    return string[::-1]

def M(string):
    new = ''
    for i in string:
        if ord(i) < 57 and ord(i) >= 48:
            new += chr(ord(i) + 1)
        elif ord(i) == 57:
            new += '0'
        else:
            new += i
    return new

def P(string):
    new = ''
    for i in string:
        if ord(i) <= 57 and ord(i) > 48:
            new += chr(ord(i) - 1)
        elif ord(i) == 48:
            new += '9'
        else:
            new += i
    return new

ans = []
for i in range(int(input())):
    to_do = input()
    message = input().strip()
    for op in to_do[::-1]:
        if op == 'C':
            message = C(message)
        if op == 'J':
            message = J(message)
        if op == 'E':
            message = E(message)
        if op == 'A':
            message = A(message)
        if op == 'P':
            message = P(message)
        if op == 'M':
            message = M(message)
    ans.append(message)

for i in ans:
    print(i)