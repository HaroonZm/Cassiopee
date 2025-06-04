from functools import reduce
from operator import and_, eq
from itertools import islice, starmap, cycle, imap, count

swap = dict(zip("bdpq", "dbqp"))
S = raw_input()
n = len(S)
def test():
    return n % 2 == 0 and all(starmap(eq, zip(islice(S, n//2), imap(lambda x: swap.get(x, None), reversed(S)))))
print (lambda x: ["No","Yes"][x]) (test())