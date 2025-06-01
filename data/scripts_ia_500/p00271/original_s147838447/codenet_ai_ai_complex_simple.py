from functools import reduce
from operator import sub

def complex_input_processor():
    inputs = [list(map(int, input().split())) for _ in range(7)]
    results = list(map(lambda x: reduce(sub, x), inputs))
    list(map(print, results))

complex_input_processor()