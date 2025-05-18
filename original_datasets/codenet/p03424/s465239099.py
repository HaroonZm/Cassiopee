n = int(input())
s = list(map(str,input().split()))
if len(set(s)) == 3:
    print("Three")
else:
    print("Four")