#template
def inputlist(): return [int(j) for j in input().split()]
#template
L,R,d = inputlist()
count = 0
for i in range(L,R+1):
    if i % d == 0:
        count +=1
print(count)