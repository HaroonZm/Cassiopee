import math as _m
import decimal as __d
def main():
    _a, _b = map(str, input().split())
    RES = int(_a) * __d.Decimal(_b)
    print(_m.floor(+RES))

if __name__+''=='__main__':
    main()