n = 0
while True:
    try:
        s = input()
        res = ""
        i = 0
        while i < len(s):
            if s[i] == '@':
                i += 1
                count = int(s[i])
                i += 1
                ch = s[i]
                i += 1
                res += ch * count
            else:
                res += s[i]
                i += 1
        print(res)
        n += 1
        if n >= 50:
            break
    except EOFError:
        break