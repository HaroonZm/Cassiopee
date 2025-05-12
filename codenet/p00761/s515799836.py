def solve(a , L , ans,a_n):
    lis = str(a)
    lis = list(lis)
    for i in range(L - len(lis)):
        lis.append('0')

    lis.sort()
    a_ = 0
    dig = 1
    for i in lis:
        a_ += int(i) * dig
        #print(type(i))
        dig *= 10

    dig = 1
    for i in reversed(lis):
        a_ -= int(i) * dig
        dig *= 10

    #print(a_ ,a)    
    for i in range(len(a_n)):
        if a_ == a_n[i]:
            print(i ,a_ ,ans - i)
            return
    a_n.append(a_)
    solve(a_ ,L ,ans+1,a_n)

while True:
    lis = input().split(' ')
    if lis[1] == '0':
        break
    a_n = [int(lis[0])]
    solve(int(lis[0]),int(lis[1]),1,a_n)