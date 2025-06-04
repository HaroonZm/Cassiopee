s = input()
ans = "No"
a = 0
while a < len(s) - 1:
    if s[a] == "A" and s[a + 1] == "C":
        ans = "Yes"
    a += 1
print(ans)