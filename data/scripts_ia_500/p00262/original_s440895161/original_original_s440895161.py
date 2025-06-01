import math

def is_sankaku(v):
    x = (math.sqrt(8*v + 1) - 1 ) / 2
    return x == int(x)

def check(lst):
    for i,v in enumerate(lst):
        if v != i + 1:
            return False
        elif i == len(lst)-1:
            return True

while 1:
    N = int(input())
    if N == 0:break
    lst = list(map(int,input().split()))
    if not is_sankaku(sum(lst)):
        print(-1)
        continue

    result = -1
    for count in range(10000):
        if check(lst):
            result = count 
            break
        spam = len(lst)
        lst = [x-1 for x in lst if x-1 > 0]
        lst.append(spam)
        
    print(result)