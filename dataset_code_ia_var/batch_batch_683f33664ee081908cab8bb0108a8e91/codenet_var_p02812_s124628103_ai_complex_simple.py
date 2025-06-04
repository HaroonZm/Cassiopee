from functools import reduce
from operator import add

_, s = map(str, [input(), input()])
indices = range(len(s)-2)
cnt = reduce(add, map(lambda i: (lambda x: x=="ABC")(s[i:i+3]), indices))
print(cnt)