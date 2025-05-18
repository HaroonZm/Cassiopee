n=int(input())
S=input().split()
S=[int(s) for s in S]

q=int(input())
T=input().split()
T=[int(t) for t in T]

#線型探索　計算時間O(qn)
def lineresearch(key):
    i = 0
    while S[i]!=key:
        i = i+1
        if i==n:
            #result = 0
            return 0
    #result = 1
    return 1

count = 0

for i in range(q):
    S.append(0)
    S[n]=T[i]   #Tの要素を番兵としておく
    count += lineresearch(S[n])
print(count)