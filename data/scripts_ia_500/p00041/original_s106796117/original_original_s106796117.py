from itertools import permutations

while(1):
    a_ = [int(i) for i in input().split()]
    if a_ == [0,0,0,0]:
        break
    p = list(list(i) for i in permutations(a_))
    cont = 1
    for a,b,c,d in p:
        if cont == 0:
            break
        for i in ("+","-","*"):
            if cont == 0:
                break
            for j in ("+","-","*"):
                if cont == 0:
                    break
                for k in ("+","-","*"):       
                    if cont == 0:
                        break
                    p = 0
                    if exec("p = (a{}b){}c{}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}){5}{2}{6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = (a{}b{}c){}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}{5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}(b{}c){}d".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}(b{}c{}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}{2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}b{}(c{}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}{1}{5}({2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = ((a{}b){}c){}d".format(i,j,k)) is None and p == 10:
                        print("(({0}{4}{1}){5}{2}){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = (a{}b){}(c{}d)".format(i,j,k)) is None and p == 10:
                        print("({0}{4}{1}){5}({2}{6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}((b{}c){}d)".format(i,j,k)) is None and p == 10:
                        print("{0}{4}(({1}{5}{2}){6}{3})".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = (a{}(b{}c)){}d".format(i,j,k)) is None and p == 10:
                        print("({0}{4}({1}{5}{2})){6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}(b{}(c{}d))".format(i,j,k)) is None and p == 10:
                        print("{0}{4}({1}{5}({2}{6}{3}))".format(a,b,c,d,i,j,k))
                        cont = 0
                    elif exec("p = a{}b{}c{}d".format(i,j,k)) is None and p == 10:
                        print("{0}{4}{1}{5}{2}{6}{3}".format(a,b,c,d,i,j,k))
                        cont = 0
    if cont == 1:
        print("0")