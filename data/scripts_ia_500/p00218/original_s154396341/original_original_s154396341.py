while True :
    n = int(input())
    if n == 0 :
        break
    
    for i in range(n) :
        m, e, j = map(int, input().split())
        if m == 100 or e == 100 or j == 100 :
            print("A")
        elif (m + e) / 2 >= 90 :
            print("A")
        elif (m + e + j) / 3 >= 80 :
            print("A")
        elif (m + e + j) / 3 >= 70 :
            print("B")
        elif (m + e + j) / 3 >= 50 and (m >= 80 or e >= 80) :
            print("B")
        else :
            print("C")