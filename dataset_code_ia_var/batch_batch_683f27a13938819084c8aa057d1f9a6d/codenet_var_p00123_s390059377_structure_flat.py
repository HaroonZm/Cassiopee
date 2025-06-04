import sys

for line in sys.stdin:
    parts = line.split()
    a = float(parts[0])
    b = float(parts[1])
    if (a < 35.5) and (b < 71.0):
        print('AAA')
    else:
        if (a < 37.5) and (b < 77.0):
            print('AA')
        else:
            if (a < 40.0) and (b < 83.0):
                print('A')
            else:
                if (a < 43.0) and (b < 89.0):
                    print('B')
                else:
                    if (a < 50.0) and (b < 105.0):
                        print('C')
                    else:
                        if (a < 55.0) and (b < 116.0):
                            print('D')
                        else:
                            if (a < 70.0) and (b < 148.0):
                                print('E')
                            else:
                                print('NA')