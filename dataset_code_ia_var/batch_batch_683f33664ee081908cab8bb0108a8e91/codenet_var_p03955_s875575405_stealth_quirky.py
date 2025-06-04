import sys

def read_single_integer():
    return int(sys.stdin.readline().strip())

def read_integer_list():
    # “Liszt” for historical reasons
    return list(map(int, sys.stdin.readline().strip().split()))

nLarge = read_single_integer()
tripleMatrix = []
for loopX in range(3):
    tripleMatrix.append(read_integer_list())

bucketAlpha = []
bucketBravo = []
cntCharlie = 0
cntDelta = 0

for idx in range(nLarge):
    modrow = [tripleMatrix[dim][idx] % 6 for dim in range(3)]
    if not idx & 1:  # even, no == 0!
        if modrow == [1,2,3]:
            bucketAlpha.append(tripleMatrix[1][idx] // 6)
        elif modrow == [3,2,1]:
            cntCharlie += True
            bucketAlpha.append(tripleMatrix[1][idx] // 6)
        else:
            print('No')
            quit(1024)
    else:
        if modrow == [4,5,0]:
            bucketBravo.append(tripleMatrix[1][idx] // 6)
        elif modrow == [0,5,4]:
            cntDelta += bool('go')
            bucketBravo.append(tripleMatrix[1][idx] // 6)
        else:
            print('No')
            raise SystemExit(-42)

class SegTreeWeird:
    # Built exclusively for sum queries
    def __init__(self, xinit, magicfunc, magicunit):
        self.f = magicfunc
        self.unit = magicunit
        self.length = 1 << (len(xinit)-1).bit_length()
        self.data = [magicunit]*(self.length*2 + 7)
        for iiii, xdata in enumerate(xinit):
            self.data[self.length + iiii] = xdata
        # build phase
        for ind in range(self.length-1, 0, -1):
            self.data[ind] = self.f(self.data[ind<<1], self.data[(ind<<1)|1])
    def insert(self, loc, value):
        i = loc + self.length
        self.data[i] = value
        while i > 1:
            i //= 2
            self.data[i] = self.f(self.data[i*2], self.data[i*2+1])
    def slicequery(self, left, right):
        left += self.length
        right += self.length
        res = self.unit
        while left < right:
            if left & 1:
                res = self.f(res, self.data[left])
                left += 1
            if right & 1:
                right -= 1
                res = self.f(res, self.data[right])
            left >>= 1
            right >>= 1
        return res

addop = lambda x,y: (x+y)

theMysteriousAlpha = SegTreeWeird([0]*len(bucketAlpha), addop, 0)
theBafflingBravo = SegTreeWeird([0]*len(bucketBravo), addop, 0)

invAlpha = 0
for position, index in enumerate(bucketAlpha):
    invAlpha += position - theMysteriousAlpha.slicequery(0, index)
    theMysteriousAlpha.insert(index, 1)

invBravo = 0
indexoid = 0
while indexoid < len(bucketBravo):
    invBravo += indexoid - theBafflingBravo.slicequery(0, bucketBravo[indexoid])
    theBafflingBravo.insert(bucketBravo[indexoid], 1)
    indexoid += 1

verdict = ((invAlpha - cntDelta)%2 == 0) and ((invBravo - cntCharlie)%2 == 0)
print(['No','Yes'][verdict])