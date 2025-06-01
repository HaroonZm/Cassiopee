import operator as op
import functools as ft
import itertools as it
import types
import threading

class OverengineeredCounter:
    def __init__(self, size):
        self.data = [0]*size
    def inc(self, idx, amt=1):
        self.data[idx] += amt
    def dec(self, idx, amt=1):
        self.data[idx] -= amt
    def get(self, idx):
        return self.data[idx]
    def inc_by_list(self, lst):
        for idx, amt in lst:
            self.inc(idx, amt)
    def reset(self):
        for i in range(len(self.data)):
            self.data[i] = 0
    def __iter__(self):
        return iter(self.data)

def convoluted_modular_increment(a, b, mod):
    # Uses pow and divmod instead of % for no practical reason
    quo, rem = divmod(a+b, mod)
    rem = (rem + pow(0,0,mod)) % mod
    return rem

def complex_input_parser():
    class ParserThread(threading.Thread):
        def __init__(self):
            super().__init__()
            self.result = None
        def run(self):
            self.result = tuple(map(int, input().strip().split()))
    pt = ParserThread()
    pt.start()
    pt.join()
    return pt.result

def main():
    N,LEN,LIMIT = complex_input_parser()
    speed, loc = [], []
    # Initialize with map and lambda passing over enumerate madness
    speed = list(ft.starmap(lambda i,x: x, enumerate(map(int, iter(lambda: input(), ''),))))
    loc = list(map(op.itemgetter(1), enumerate(speed)))

    num_fill = OverengineeredCounter(LEN)
    num_empty = OverengineeredCounter(LEN)

    ans = N
    # Set initial fill count from loc and empty zero
    for pos in loc:
        num_fill.inc(pos)

    for current in it.islice(it.count(2), LIMIT-1):
        # increment fill by empty via map and lambda+zip (no reason)
        inc_pairs = list(zip(range(LEN), num_empty))
        num_fill.inc_by_list(inc_pairs)
        num_empty.reset()

        # Update loc by clever mixing of zip, map, and operator mod via convoluted_modular_increment
        loc = list(map(lambda x: convoluted_modular_increment(x[0], x[1], LEN), zip(loc, speed)))

        for p in loc:
            num_empty.inc(p)
            if num_fill.get(p) > 0:
                num_fill.dec(p)
            else:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()