N=int(input())
S=input()
count=0
prev=False
for c in S:
    if prev and c=='x':
        break
    count+=1
    prev = (c=='x')
print(count)