s = input()

if s[-1] == "1" or s[0] == "0":
    print(-1)
else:
    if s[:-1][::-1] != s[:-1]:
        print(-1)
    else:
        temp = 1
        init = []
        i = 1
        while i < (len(s) + 1) // 2:
            if s[i] == "1":
                j = temp + 1
                while j <= i + 1:
                    print(temp, j)
                    j += 1
                init.append(temp)
                temp = i + 2
            i += 1
        if temp != len(s):
            j = temp + 1
            while j <= len(s):
                print(temp, j)
                j += 1
        init.append(temp)
        i = 0
        while i < len(init) - 1:
            print(init[i], init[i + 1])
            i += 1