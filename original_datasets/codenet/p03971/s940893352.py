n,a,b=map(int,input().split())
s=input()
acnt=0
bcnt=0
for i in range(len(s)):
  if s[i]=="a":
    if acnt+bcnt<a+b:
      print("Yes")
      acnt+=1
    else:
      print("No")
  elif s[i]=="b":
    if acnt+bcnt<a+b and bcnt<b:
      print("Yes")
      bcnt+=1
    else:
      print("No")
  else:
    print("No")