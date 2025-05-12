s=input()
ans="No"
for a in range(len(s)-1):
  if s[a]=="A" and s[a+1]=="C":
    ans="Yes"
print(ans)