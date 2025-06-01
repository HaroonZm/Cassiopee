while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        line = input()
        parts = line.split()
        m = int(parts[0])
        e = int(parts[1])
        j = int(parts[2])

        if m == 100 or e == 100 or j == 100:
            print("A")
        else:
            average_me = (m + e) / 2
            average_all = (m + e + j) / 3

            if average_me >= 90:
                print("A")
            elif average_all >= 80:
                print("A")
            elif average_all >= 70:
                print("B")
            elif average_all >= 50 and (m >= 80 or e >= 80):
                print("B")
            else:
                print("C")