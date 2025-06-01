from __future__ import division,print_function
try:
    input = raw_input
    range = xrange
except NameError:
    pass

a=[0]*100
while True:
    inp = int(input())
    if inp == 0:
        break
    if inp == 1:
        a[1] = 1
        val = 1
    elif inp == 2:
        a[2] = 2
        val = 2
    elif inp == 3:
        a[3] = 4
        val = 4
    else:
        if a[inp] != 0:
            val = a[inp]
        else:
            # calculate values for smaller stairs if needed
            if a[inp-1] == 0:
                if inp-1 == 1:
                    a[1] = 1
                elif inp-1 == 2:
                    a[2] = 2
                elif inp-1 == 3:
                    a[3] = 4
                else:
                    if a[inp-4] == 0:
                        if inp-4 == 1:
                            a[1] = 1
                        elif inp-4 == 2:
                            a[2] = 2
                        elif inp-4 == 3:
                            a[3] = 4
                        else:
                            # just assume a[inp-4] zero or not zero - to keep flat
                            pass
                    if a[inp-3] == 0:
                        if inp-3 == 1:
                            a[1] = 1
                        elif inp-3 == 2:
                            a[2] = 2
                        elif inp-3 == 3:
                            a[3] = 4
                        else:
                            pass
                    a[inp-1] = a[inp-4] + a[inp-3] + a[inp-2] if (inp-4)>0 and (inp-3)>0 and (inp-2)>0 else 0
            if a[inp-2] == 0:
                if inp-2 == 1:
                    a[1] = 1
                elif inp-2 == 2:
                    a[2] = 2
                elif inp-2 == 3:
                    a[3] = 4
            if a[inp-3] == 0:
                if inp-3 == 1:
                    a[1] = 1
                elif inp-3 == 2:
                    a[2] = 2
                elif inp-3 == 3:
                    a[3] = 4
            a[inp] = a[inp-3] + a[inp-2] + a[inp-1]
            val = a[inp]
    print(val//3650+1)