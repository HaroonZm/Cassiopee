from functools import reduce

def calc():
 N,T=map(int,input().split())
 arr = [int(x) for x in input().split()]
 total = 0
 i=0
 while i<len(arr)-1:
    diff=arr[i+1]-arr[i]
    if diff<T:total+=diff
    else: total+=T
    i+=1
 return total+T

def main():
    print(calc())

main()