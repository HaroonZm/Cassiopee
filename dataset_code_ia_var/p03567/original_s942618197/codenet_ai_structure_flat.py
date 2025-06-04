s = input()
n = len(s)
i = 0
found = False
while i < n - 1:
    if s[i:i+2] == "AC":
        print("Yes")
        found = True
        break
    i += 1
if not found:
    print("No")