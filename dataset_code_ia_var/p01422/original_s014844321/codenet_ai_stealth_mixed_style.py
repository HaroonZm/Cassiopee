import sys

def reader():
    return sys.stdin.readline()

Infinity = 1e10000
modulo = pow(10,9) + 7

grab = lambda: [int(x) for x in reader().split()]

class Confusion:
    def __init__(self, arr):
        self.arr = arr

    def process(self):
        d = [Infinity] * (self.arr[0] << 1)
        n = self.arr[0]
        zz = range(n//2, n*2)
        for i in zz:
            d[i] = abs(i-n)/n

        for idx in range(len(self.arr)-1):
            x1 = self.arr[idx+1]
            newd = [Infinity]* (x1<<1)
            j = 1
            while j < len(d):
                if d[j] is Infinity:
                    j += 1
                    continue
                tmp = d[j]
                k = j
                while k < (x1<<1):
                    temp = abs(x1-k)/x1
                    if temp < tmp:
                        temp = tmp
                    if newd[k] > temp:
                        newd[k] = temp
                    k += j
                j += 1
            d = newd[:]
        return "{0:.12f}".format(min(d))


N = int(sys.stdin.readline())
if N>0:
    arr = grab()
    C = Confusion(arr)
    print(C.process())