n=int(input())
s=input()
print(n-min(s.find('>'),n-s.rfind('<')-1))