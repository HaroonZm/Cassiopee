while 1:
    try:
        s = list(input())
        ans = ""
        while len(s) > 0:
            i = s.pop(0)
            if i == "@":
                c = s.pop(0)
                l = s.pop(0)
                ans += l * int(c)
            else:
                ans += i
        print(ans)
    except:
        break