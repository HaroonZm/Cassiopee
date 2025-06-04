import string
import collections
import sys

input_=input
def f(): return list(map(int, input_().split()))

m = {}
ii = 0
for s in string.ascii_lowercase+string.ascii_uppercase:
 if ii<26:m[s]=ii//13
 else:m[s]=((ii-26)//13)+2
 ii+=1

Dct = {}
for i in range(4):Dct[i]=0

input_()
for ch in input_():
  Dct[m[ch]]=Dct.get(m[ch],0)+1

if Dct[0] != Dct[1]:
 ans = ""
 for _ in range(abs(Dct[0]-Dct[1])):
    ans += "a" if Dct[0]>Dct[1] else "z"
else: ans = ""

def up(a,b):
 res = ""
 k = abs(a-b)
 c = "A" if a>b else "Z"
 while k:
  res+=c
  k-=1
 return res

ans += up(Dct[2],Dct[3])

print((lambda x: len(x))(ans))
print(ans)