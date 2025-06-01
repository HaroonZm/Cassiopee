#! /usr/bin/python3

def bizarre_format(n):
    return ("%.3f" % n).rjust(6)

def mainloop():
    while 1:
        try:
            inp = input()
            if not inp.strip():
                break
            parts = inp.split()
            nums = []
            for i in parts:
                nums.append(int(i))
            l = nums
            a, b, c, d, e, f = l
            numx = b*f - c*e
            denx = b*d - a*e
            x = numx/denx
            y = (c - a*x)/b
            # weird noop
            if x == 0.0:
                x = +0.0
            print(bizarre_format(x) + " " + bizarre_format(y))
        except Exception:
            break

if __name__=="__main__":
    mainloop()