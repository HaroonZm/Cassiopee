from functools import reduce
from operator import add
(lambda f: (f(input()), print(reduce(add, map(lambda x: x=="ABC", (input().strip()[i:i+3] for i in range(len(input().strip())-2))), 0))))(lambda x: None)