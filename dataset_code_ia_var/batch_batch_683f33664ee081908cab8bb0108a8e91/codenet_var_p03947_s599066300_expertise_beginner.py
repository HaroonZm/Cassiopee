s = input()
length = len(s)
count = 0
i = 0

if s[0] == "B":
    while i < length - 1:
        if s[i] == "B" and s[i+1] == "W":
            count = count + 1
            i = i + 2
        else:
            i = i + 1
    if s[length-1] == "W":
        print(str(count * 2 - 1))
    else:
        print(str(count * 2))
else:
    while i < length - 1:
        if s[i] == "W" and s[i+1] == "B":
            count = count + 1
            i = i + 2
        else:
            i = i + 1
    if s[length-1] == "B":
        print(str(count * 2 - 1))
    else:
        print(str(count * 2))