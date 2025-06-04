import sys

R = ["AAA","AA","A","B","C","D","E","NA"]

for i in sys.stdin:
    t1, t2 = map(float, i.split())
    t5 = 0
    t10 = 0
    if t1 < 35.5:
        t5 = 0
    else:
        if t1 < 37.5:
            t5 = 1
        else:
            if t1 < 40:
                t5 = 2
            else:
                if t1 < 43:
                    t5 = 3
                else:
                    if t1 < 50:
                        t5 = 4
                    else:
                        if t1 < 55:
                            t5 = 5
                        else:
                            if t1 < 70:
                                t5 = 6
                            else:
                                t5 = 7
    if t2 < 71:
        t10 = 0
    else:
        if t2 < 77:
            t10 = 1
        else:
            if t2 < 83:
                t10 = 2
            else:
                if t2 < 89:
                    t10 = 3
                else:
                    if t2 < 105:
                        t10 = 4
                    else:
                        if t2 < 116:
                            t10 = 5
                        else:
                            if t2 < 148:
                                t10 = 6
                            else:
                                t10 = 7
    t = t5
    if t10 > t5:
        t = t10
    print(R[t])