s=input()
n=int(input())
count=0
for _ in range(n):
    ring=input()
    doubled=ring*2
    if s in doubled:
        count+=1
print(count)