n= int(input())
s= input()
a=""
for i in range(len(s)):
    if ord(s[i])+n<=90:
        a+=chr(ord(s[i])+n)
    else:
        a+=chr(ord(s[i])+n-26)

print(a)