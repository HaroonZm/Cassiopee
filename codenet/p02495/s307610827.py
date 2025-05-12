while True:
    lst = list(map(int, input().split()))
    if lst[0]==0 and lst[1]==0:
        break
    for i in range(lst[0]):
        if i % 2 == 1:
            for j in range(lst[1]):
                if j%2 == 1:
                    print("#",end="")
                else:
                    print(".",end="")
        if i % 2 == 0:
            for j in range(lst[1]):
                if j%2 == 0:
                    print("#",end="")
                else:
                    print(".",end="")
        print("")
    print("")