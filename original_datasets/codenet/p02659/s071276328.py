from math import floor
from decimal import Decimal
if __name__ == '__main__':

    a, b = input().split()
    a = int(a)
    b = Decimal(b)
    print(floor(a * b))