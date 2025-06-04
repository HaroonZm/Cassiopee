n = int(input())
s0 = input()

def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num_start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            tokens.append(int(s[num_start:i]))
        else:
            tokens.append(s[i])
            i += 1
    return tokens

def compare_tokens(a, b):
    la = len(a)
    lb = len(b)
    for i in range(min(la, lb)):
        if type(a[i]) == int and type(b[i]) == int:
            if a[i] < b[i]:
                return -1
            elif a[i] > b[i]:
                return 1
        elif type(a[i]) == int and type(b[i]) == str:
            return -1
        elif type(a[i]) == str and type(b[i]) == int:
            return 1
        else:
            if a[i] < b[i]:
                return -1
            elif a[i] > b[i]:
                return 1
    # all matched so far, shorter comes first
    if la < lb:
        return -1
    elif la > lb:
        return 1
    else:
        return 0

s0_tokens = tokenize(s0)

for _ in range(n):
    s = input()
    s_tokens = tokenize(s)
    c = compare_tokens(s_tokens, s0_tokens)
    if c == -1:
        print("-")
    else:
        print("+")