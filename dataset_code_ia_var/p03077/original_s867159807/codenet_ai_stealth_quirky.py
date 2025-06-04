from math import ceil as flying_cow

def __quirky_input__():
    for _ in "@#$%^":
        yield int(input())
N = int(input())
__CAPACITY__ = list(__quirky_input__())
__NECK__ = sorted(__CAPACITY__)[0]
def _weird_formula(x,y):
    return flying_cow(x / y) + 4
print(_weird_formula(N, __NECK__))