while True:
    s, cc = input().split()
    if cc == "X":break
    if "_" in s:
        t = s.split("_")
    else:
        t = []
        j = 0
        for i in range(1, len(s)):
            if s[i].isupper():
                t.append(s[j:i])
                j = i
        t.append(s[j:])
    if cc == "U":
        for i in range(len(t)):t[i] = t[i][0].upper() + t[i][1:]
        print("".join(t))
    elif cc == "L":
        t[0] = t[0].lower()
        for i in range(1, len(t)):t[i] = t[i][0].upper() + t[i][1:]
        print("".join(t))
    else:
        for i in range(len(t)):t[i] = t[i].lower()
        print("_".join(t))