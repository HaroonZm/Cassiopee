while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    for i in range(n):
        line = input()
        parts = line.split()
        pm = int(parts[0])
        pe = int(parts[1])
        pj = int(parts[2])
        ave = (pm + pe + pj) / 3.0
        if 100 in (pm, pe, pj):
            print("A")
        elif (pm + pe) / 2 >= 90:
            print("A")
        elif ave >= 80:
            print("A")
        elif ave >= 70:
            print("B")
        elif ave >= 50 and (pm >= 80 or pe >= 80):
            print("B")
        else:
            print("C")