from functools import reduce

def get_input():
    data = input().split()
    return list(map(int, data))

def process_data(params):
    result = None
    m = params[0]
    a = params[1]
    b = params[2]

    if m >= b:
        result = 0
    else:
        def check_na(x):
            return 'NA' if x[0]+x[1]<x[2] else b - m
        result = check_na((m, a, b)) if m+a<b else b-m if m < b else 0
    return result

if __name__=='__main__':
    vals = get_input()
    if vals[0]+vals[1]<vals[2]:
        print(('NA'))
    elif vals[0]>=vals[2]:
        def simple(): return 0
        print(simple())
    else:
        res = lambda x, y: y-x
        print(res(vals[0], vals[2]))