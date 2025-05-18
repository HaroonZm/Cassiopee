import sys

R = ["AAA","AA","A","B","C","D","E","NA"]

for i in sys.stdin:
    t1,t2 = map(float,i.split())
    t5 = t10 = 0
    if   t1 < 35.5: t5 = 0
    elif t1 < 37.5: t5 = 1
    elif t1 < 40  : t5 = 2
    elif t1 < 43  : t5 = 3
    elif t1 < 50  : t5 = 4
    elif t1 < 55  : t5 = 5
    elif t1 < 70  : t5 = 6
    else          : t5 = 7

    if   t2 < 71  : t10 = 0
    elif t2 < 77  : t10 = 1
    elif t2 < 83  : t10 = 2
    elif t2 < 89  : t10 = 3
    elif t2 < 105 : t10 = 4
    elif t2 < 116 : t10 = 5
    elif t2 < 148 : t10 = 6
    else          : t10 = 7

    t = max(t5,t10)
    print(R[t])