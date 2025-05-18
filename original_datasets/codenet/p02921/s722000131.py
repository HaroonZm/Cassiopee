s = input()
t = input()
ans = 0
ans += 1 if s[0]==t[0] else 0
ans += 1 if s[1]==t[1] else 0
ans += 1 if s[2]==t[2] else 0
print(ans)