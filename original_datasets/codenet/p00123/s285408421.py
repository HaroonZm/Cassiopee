while True:
    try:
        t1, t2 = map(float, input().split())
    except:
        break
    t1, t2 = int(t1*100), int(t2*100)
    if t1 < 3550 and t2 < 7100:
        print("AAA")
    elif t1 < 3750 and t2 < 7700:
        print("AA")
    elif t1 < 4000 and t2 < 8300:
        print("A")
    elif t1 < 4300 and t2 < 8900:
        print("B")
    elif t1 < 5000 and t2 < 10500:
        print("C")
    elif t1 < 5500 and t2 < 11600:
        print("D")
    elif t1 < 7000 and t2 < 14800:
        print("E")
    else:
        print("NA")