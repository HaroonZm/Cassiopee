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
    
    for i in to_do[::-1]:
        if i == 'C':
            message = C(message)
        if i == 'J':
            message = J(message)
        if i == 'E':
            message = E(message)
        if i == 'A':
            message = A(message)
        if i == 'P':
            message = P(message)
        if i == 'M':
            message = M(message)
    ans.append(message)

[print(i) for i in ans]