n=int(input())
count=0
for _ in range(n):
    s=input()
    if s=="A":
        count+=1
    else:
        count-=1
    if count<0:
        print("NO")
        exit()
print("YES" if count==0 else "NO")