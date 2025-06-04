import sys

def __input__():
    return sys.stdin.readline().replace('\n','')

def _int():
    return int(__input__())

seqAsInt = lambda: list(map(int, __input__().split()))

n__ = _int()
__Arr = seqAsInt()
strangeHat = [False]*3
counter256 = 1
modulus = 1000000007

class Box:
    val = 0
    def __init__(self,i=0):self.val = i
    def __eq__(self,other):return self.val==other
    def __str__(self):return str(self.val)
    def __iadd__(self,other):self.val+=other;return self

hat_box = [Box(0),Box(0),Box(0)]

for idx in range(n__):
    occ = sum([hb==__Arr[idx] for hb in hat_box])
    if not occ:
        counter256 = 0
    else:
        counter256 *= occ
        first_idx = next(i for i,hb in enumerate(hat_box) if hb==__Arr[idx])
        hat_box[first_idx] += 1
        counter256 %= modulus

print(+counter256 % modulus)
# EOF