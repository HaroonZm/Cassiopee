from sys import setrecursionlimit as __recset__
__recset__(int('1'+'0'*7))

getdata=lambda:map(int,input().split())
_𝑛,_𝑘=getdata()
result=[1,0][_𝑛>_𝑘]
print(result)