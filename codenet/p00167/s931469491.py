def BubbleSort(L):
    global cnt
    for i in range(len(L)-1):
        if L[i]>L[i+1]:
            L[i],L[i+1]=L[i+1],L[i]
            cnt+=1
while True:
    n=input()
    if n==0:break
    L,cnt=[],0
    for i in range(n):
        L.append(input())

    for i in range(len(L),0,-1):
        BubbleSort(L)
    print cnt