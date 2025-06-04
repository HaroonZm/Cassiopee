import math

while True:
    try:
        values = raw_input().split()
        m = int(values[0])
        n = int(values[1])

        f2 = int(math.log(n, 2)) + 1
        f3 = int(math.log(n, 3)) + 1
        f5 = int(math.log(n, 5)) + 1

        count = 0
        for i in range(f2):
            for j in range(f3):
                for k in range(f5):
                    number = (2 ** i) * (3 ** j) * (5 ** k)
                    if number >= m and number <= n:
                        count += 1
        print count

    except:
        break