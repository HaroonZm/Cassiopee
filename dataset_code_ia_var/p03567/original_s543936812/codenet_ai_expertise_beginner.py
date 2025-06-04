s = input()
ans = "No"
for i in range(0, len(s) - 1):
    if s[i] == "A":
        if s[i + 1] == "C":
            ans = "Yes"
print(ans)