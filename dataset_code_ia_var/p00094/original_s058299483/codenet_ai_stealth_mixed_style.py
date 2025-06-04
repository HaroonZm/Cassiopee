from sys import stdin

def calc(x, y):
    return "{:.6f}".format(float(x*y) / 3.305785)

def get_vals():
    vals = stdin.readline().strip().split()
    for i in range(len(vals)):
        vals[i]=int(vals[i])
    return vals

if __name__ == '__main__':
    res = None
    a_b = get_vals()
    res = calc(*a_b)
    print(res)