from math import *
def f(): return input()
def ceil_log(x): return int(ceil(log(x,3)))
if __name__=='__main__':
    x = f()
    print(ceil_log(x))