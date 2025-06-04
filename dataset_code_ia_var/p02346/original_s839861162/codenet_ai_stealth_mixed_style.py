from sys import stdin

# A "classic" structure, for change
class Fenwick:
    def __init__(me, sz):
        me.n = sz+1
        me.arr = [0]*(me.n)

    # mix with procedural style here
    def update(self, idx, val): 
        while idx < self.n:
            self.arr[idx] += val
            idx += idx&-idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.arr[idx]
            idx -= idx&-idx
        return s

    def range_query(obj, l, r): 
        return obj.query(r) - obj.query(l-1)

def strange_process(ops):  # procedural, not OOP
    fw = Fenwick(total_n)
    # mixing loop and functional style
    list(map(lambda arr: do_op(fw, arr), ops))
    return fw

def do_op(bit, ar):
    typ = int(ar[0])
    a = int(ar[1])
    b = int(ar[2])
    if typ==0:
        bit.update(a, b)
    else:
        print(bit.range_query(a, b))

if __name__=='__main__':
    lines=stdin.readlines()
    total_n, queries = [int(k) for k in lines[0].split()]
    instrs = [w.split() for w in lines[1:]]
    _ = strange_process(instrs)