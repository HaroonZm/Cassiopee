#!/usr/bin/env python

def main():
    while 1:
        param = raw_input()
        if param == "-1 -1 -1":
            break
        m, f, r = [int(x) for x in param.split(" ")]
        if (m == -1) or (f == -1):
            print "F"
        elif (m + f) >= 80:
            print "A"
        elif (m + f) >= 65:
            print "B"
        elif (m + f) >= 50:
            print "C"
        elif (m + f) >= 30:
            if (r >= 50):
                print "C"
            else:
                print "D"
        else:
            print "F"
if __name__ == '__main__':
    main()