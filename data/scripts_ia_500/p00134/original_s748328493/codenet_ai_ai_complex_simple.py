N = int(__import__('functools').reduce(lambda x, y: x+y, map(lambda z: ord(z)-48, str(__import__('sys').stdin.read(1)))))
from operator import add
print((lambda f, l: f(f, l, 0, 0))(lambda self, lst, i, s: (s / len(lst)) if i == len(lst) else self(self, lst, i+1, add(s, int(lst[i]))), [int(__import__('sys').stdin.readline().strip()) for _ in range(N)]))