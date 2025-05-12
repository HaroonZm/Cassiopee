lst = list(map(int, input().split()))
if lst[0] + lst[1]*5 + lst[2]*10 + lst[3]*50 + lst[4]*100 + lst[5]*500 >= 1000 :
    print(1)
else :
    print(0)