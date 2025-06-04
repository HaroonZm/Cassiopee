N=int(input())
h=[int(x) for x in input().split()]
answer=0
def all_zero(arr):
    for x in arr:
        if x!=0:
            return False
    return True
def paint(l):
    idx=0
    while idx<len(l):
        if l[idx]==0: idx+=1; continue
        else:
            globals()['answer']+=1
            j=idx
            while j<len(l) and l[j]>0:
                l[j]-=1; j+=1
            idx=j
while not all_zero(h):
    paint(h)
print(answer)