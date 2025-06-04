s = input()
found = False
i = 0
while i < len(s) - 1:
    if s[i] == "A" and s[i + 1] == "C":
        found = True
        break
    i = i + 1
if found:
    print("Yes")
else:
    print("No")