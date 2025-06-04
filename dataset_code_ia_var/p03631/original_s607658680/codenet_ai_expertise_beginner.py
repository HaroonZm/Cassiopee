s = input()
if len(s) > 0:
    if s[0] == s[len(s)-1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")