import os
import sys
import math

filename = sys.argv[1] if len(sys.argv) > 1 else None
test_mode = filename is not None
buffer = []
cases = 1
if test_mode:
    with open(filename) as ff:
        blank_flg = False
        for line in ff:
            line = line.strip()
            if line:
                buffer.append(line)
                blank_flg = False
            else:
                if not blank_flg:
                    cases += 1
                blank_flg = True

def readline():
    if test_mode:
        return buffer.pop(0)
    else:
        return raw_input()

while True:
    try:
        n = int(readline())
        if n == 0:
            break
        ary = []
        for _ in range(n):
            ary.append([float(x) for x in readline().split()])
        x_min = -100.0
        x_max = 100.0
        for _ in range(60):
            c1 = (x_min * 2 + x_max) / 3
            c2 = (x_min + x_max * 2) / 3
            # inline search_y
            y_min_1 = -100.0
            y_max_1 = 100.0
            for __ in range(60):
                y_c1 = (y_min_1*2 + y_max_1)/3
                y_c2 = (y_min_1 + y_max_1*2)/3
                # inline calc
                min1 = float('inf')
                for item in ary:
                    v = item[2]**2 - (item[0]-c1)**2 - (item[1]-y_c1)**2
                    if v < min1:
                        min1 = v
                min2 = float('inf')
                for item in ary:
                    v = item[2]**2 - (item[0]-c1)**2 - (item[1]-y_c2)**2
                    if v < min2:
                        min2 = v
                if min1 > min2:
                    y_min_1 = y_c1
                else:
                    y_max_1 = y_c2
            # after search_y for c1
            min_final1 = float('inf')
            for item in ary:
                v = item[2]**2 - (item[0]-c1)**2 - (item[1]-y_max_1)**2
                if v < min_final1:
                    min_final1 = v

            y_min_2 = -100.0
            y_max_2 = 100.0
            for __ in range(60):
                y_c1 = (y_min_2*2 + y_max_2)/3
                y_c2 = (y_min_2 + y_max_2*2)/3
                min1 = float('inf')
                for item in ary:
                    v = item[2]**2 - (item[0]-c2)**2 - (item[1]-y_c1)**2
                    if v < min1:
                        min1 = v
                min2 = float('inf')
                for item in ary:
                    v = item[2]**2 - (item[0]-c2)**2 - (item[1]-y_c2)**2
                    if v < min2:
                        min2 = v
                if min1 > min2:
                    y_min_2 = y_c1
                else:
                    y_max_2 = y_c2
            min_final2 = float('inf')
            for item in ary:
                v = item[2]**2 - (item[0]-c2)**2 - (item[1]-y_max_2)**2
                if v < min_final2:
                    min_final2 = v

            if min_final1 > min_final2:
                x_max = c2
            else:
                x_min = c1
        # result for x_max
        y_min = -100.0
        y_max = 100.0
        for _ in range(60):
            c1y = (y_min*2 + y_max)/3
            c2y = (y_min + y_max*2)/3
            min1 = float('inf')
            for item in ary:
                v = item[2]**2 - (item[0]-x_max)**2 - (item[1]-c1y)**2
                if v < min1:
                    min1 = v
            min2 = float('inf')
            for item in ary:
                v = item[2]**2 - (item[0]-x_max)**2 - (item[1]-c2y)**2
                if v < min2:
                    min2 = v
            if min1 > min2:
                y_min = c1y
            else:
                y_max = c2y
        min_final = float('inf')
        for item in ary:
            v = item[2]**2 - (item[0]-x_max)**2 - (item[1]-y_max)**2
            if v < min_final:
                min_final = v
        print(math.sqrt(min_final))
    except Exception:
        break