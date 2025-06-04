from functools import reduce
import re
s = ''.join(map(chr, map(ord, input())))
s = reduce(lambda a, _: a.replace(',', ' '), range(1), s)
print(''.join(re.findall(r'[^, ]+| ', s)))