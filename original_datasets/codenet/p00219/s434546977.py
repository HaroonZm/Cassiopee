while True :
    n = int(input())
    if n == 0 : break
    numList = [0 for i in range(10)] 
    for i in range(n) :
        c = int(input())
        numList[c] += 1

    for i in range(10) :
        cnt = '*' * numList[i] 
        if len(cnt) == 0 : print("-")
        else : print(cnt)