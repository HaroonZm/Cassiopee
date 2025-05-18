def Com(a, b) :
    list_a = list(a)
    list_b = list(b)
    list_a.reverse()
    list_b.reverse()
    while '*' in list_a :
        list_a.remove('*')
    
    ans = True
    for i in range(len(list_a)) :
        if list_a[i] != list_b[i] :
            ans = False
            break
    return ans

while True :
    n, m = map(int, input().split())
    if n == 0 and m == 0 :
        break

    atari = []
    money = []
    for i in range(n) :
        a, b = input().split()
        atari.append(a)
        money.append(int(b))

    cost = 0
    for i in range(m) :
        s = input()
        for j in range(n) :
            if Com(atari[j], s) == True :
                cost += money[j]
    print(cost)