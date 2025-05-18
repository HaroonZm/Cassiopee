s = input()
n = len(s)
for i in range(n - 1):
    if s[i : i + 2] == "AC":
        print("Yes")
        break
else:
    print("No")