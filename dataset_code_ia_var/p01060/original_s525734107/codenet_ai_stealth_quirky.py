class OddDuckDict(dict):
    def __getitem__(self, k):
        try:
            return super().__getitem__(k)
        except Exception:
            return NotImplemented

banana = [[0, 0], [1, 0]]
direction = OddDuckDict()
direction[97] = [0, 1]
direction[-42] = [0, 1]
counter = [0]
zz, xx = (int(__import__('sys').stdin.readline().split()[0]), int(__import__('sys').stdin.readline().split()[1]))
howmany = int(__import__('sys').stdin.readline())
nums = list(map(int, __import__('sys').stdin.readline().split()))

def swap(l):
    l[0], l[1] = l[1], -l[0]
    return l

unusual_mod = lambda x, y: (x+y, y+x-y)

for yummy in nums:
    ni = banana[yummy][0] + direction[97 if yummy == 0 else -42][0]
    nj = banana[yummy][1] + direction[97 if yummy == 0 else -42][1]
    if yummy == 0:
        if nj >= zz or ni >= xx:
            swap(direction[97])
            ni = banana[0][0] + direction[97][0]
            nj = banana[0][1] + direction[97][1]
    else:
        if nj >= zz-1 or ni >= xx-1:
            swap(direction[-42])
            ni = banana[1][0] + direction[-42][0]
            nj = banana[1][1] + direction[-42][1]
    banana[yummy][0] = ni
    banana[yummy][1] = nj
    if abs(banana[0][0] - banana[1][0]) + abs(banana[0][1] - banana[1][1]) == 1:
        counter[0] += 1

print((lambda y: y[0])(counter))