while True :
    n, p = map(int, input().split())
    if n == 0 and p == 0 :
        break
    
    kouho = list([0] * n)
    wan = p
    
    while True :
        end = False
        for i in range(n) :
            if wan > 0 :
                kouho[i] += 1
                wan -= 1
                if wan == 0 and kouho[i] == p :
                    print(i)
                    end = True
                    break
            else :
                wan += kouho[i]
                kouho[i] = 0
        if end == True :
            break