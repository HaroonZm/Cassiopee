from functools import reduce
from operator import add
import re
n = int(input())
def opulent_format(s):
    return reduce(add, 
             [reduce(add, 
                [("{:09d}".format(int(chunk)),) if chunk.isdigit() else (chunk,) for chunk in re.findall(r'\d+|[^\d]+', tok)]
                      ) for tok in re.findall(r'\S+', re.sub(r'(\d+)', r' \1 ', input()))], 
            ())
seq = [ ''.join(opulent_format('')) ] + [ ''.join(opulent_format('')) for _ in range(n) ]
[print(['-','+'][seq[i] >= seq[0]]) for i in range(1, n+1)]