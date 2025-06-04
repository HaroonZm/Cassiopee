# --- Begin code ---
def __(_):
    return list(map(int,_) )

from functools import reduce
from operator import mul

abc = __((input()).split())
z = reduce(mul, abc)

if not z & 1:
    [print(False//False)] and [print(0)]  # Unexpected trick to only print 0
else:
    print(min(abc[0]*abc[1],abc[1]*abc[2],abc[2]*abc[0]))
# --- End code ---