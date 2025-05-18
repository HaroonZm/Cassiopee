clst = [10,50,100,500]
def sgn(t):
    for I in range(0,4):
        if clst[I] == t:
            return I
def cnt(l1,l2,N): 
    s = sgn(l1[N])
    l2[s] = l2[s] + 1
def shiharai(bill,purse):
    B = bill
    lst1 = []
    lst2 = [0]
    for i in range(0,4):
        for j in range(0,purse[i]):
            lst1.append(clst[i])
    lst2[0] = lst1[0]
    for i in range(1,len(lst1)):
        k = lst1[i] + lst2[i-1]
        lst2.append(k)
    pay = [0,0,0,0]
    while B > 0:
        i = 0
        while lst2[i] < B:
            i = i + 1
        if lst2[i] == B:
            for j in range(0,i+1):
                cnt(lst1,pay,j)
                B = B - lst1[j]
        else:
            cnt(lst1,pay,i)
            B = B - lst1[i]
    for i in range(4):
        purse[i] = purse[i] - pay[i]
    purse[0] = purse[0] - B//10
    return purse
def exchng(purse,n,r):
    while purse[n] >= r:
        purse[n] = purse[n] - r
        purse[n+1] = purse[n+1] + 1
def ryogae(purse):
    exchng(purse,0,5)
    exchng(purse,1,2)
    exchng(purse,2,5)
    return purse
L = 0
while True:
    bill = int(input().strip())
    if bill == 0:
        break
    if L != 0:
        print()
    lst = list(map(int,input().strip().split(" ")))
    purse = [0,0,0,0]
    for A in range(0,4):
        purse[A] = lst[A]
    purse = shiharai(bill,purse)
    purse = ryogae(purse)
    shouldpay = [0,0,0,0]
    for B in range(0,4):
        if lst[B] > purse[B]:
            shouldpay[B] = lst[B] - purse[B]
    for i in range(0,4):
        if shouldpay[i] != 0:
            print(clst[i],shouldpay[i])
    L = L + 1