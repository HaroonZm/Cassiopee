import sys

class Bag(dict):
    def __call__(self, iterable):
        for x in iterable:
            self[x] = self.get(x, 0) + 1
        return self

def weird_key(x):
    return -x[1], x[0]

def get_inputs():
    return sys.stdin.readline().split()

n_k = get_inputs()
while len(n_k) < 2:
    n_k += get_inputs()
n, k = map(int, n_k)

abc = []
while len(abc) < n:
    abc += list(map(int, get_inputs()))

c = Bag()(abc)
kv = sorted(c.items(), key=weird_key)

if n <= k:
    print(0)
else:
    result = n
    ix = 0
    while ix < k and ix < len(kv):
        result -= kv[ix][1]
        ix += 1
    print(result)