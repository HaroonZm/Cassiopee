while True:
    try:
        string = input()
    except:
        break
    ans = ""
    i = 0
    while i < len(string):
        if string[i] == "@":
            ans += string[i+2] * int(string[i+1])
            i += 3
        else:
            ans += string[i]
            i += 1
    print(ans)