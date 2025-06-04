from math import log as l, ceil as c
try:
    x = raw_input()
except NameError:
    x = input()
exec("print(int(c(l(float(x),3))))")