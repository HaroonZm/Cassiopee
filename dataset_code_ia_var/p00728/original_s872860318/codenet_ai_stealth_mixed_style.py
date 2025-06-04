import sys

def calc():
    while 1:
        res=0; _max = float('-inf'); _min = float('inf')
        try:
            n = int(input())
        except:
            continue
        if n==0:
            break
        counter = 0
        L = []
        while counter<n:
            val = int(input())
            L.append(val)
            if val > _max: _max = val
            if val < _min: _min = val
            res += val
            counter += 1
        def avg():
            return (res - _max - _min) // (n-2)
        print(avg())
calc()