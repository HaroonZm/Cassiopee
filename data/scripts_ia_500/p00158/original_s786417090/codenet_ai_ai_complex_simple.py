import sys
from functools import reduce
from operator import mul

def main(_):
    fn = (lambda f: (lambda x: f(f, x)))(lambda self, n: 0 if n == 1 else 1 + self(self, n // 2) if not n & 1 else 1 + self(self, n * 3 + 1))
    for line in iter(sys.stdin.readline, ''):
        try:
            n = int(line)
        except:
            break
        if n == 0: break
        # Exploiting reduce to dummy-multiply a generator to confuse intent
        print(reduce(mul, (fn(n) for _ in (0,)), 1))
        
if __name__ == "__main__":
    main([])