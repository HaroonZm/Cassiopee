import sys
input = sys.stdin.readline

# Ok, let's try to implement a Binary Indexed Tree (Fenwick Tree), I hope I do it right
class BIT:
    def __init__(self, size):
        # maybe could've called it n but "size" is clearer for me I guess
        self.size = size
        self.tree = [0]*(size + 1)
        self.arr = [0]*(size + 1)  # not sure I really need this

    def add(self, idx, val):
        # supposed to be 1-indexed -- frustrating...
        self.arr[idx] += val
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx  # bit twiddling, hope no bugs here

    # I always forget if this is inclusive or not, pretty sure yes
    def getsum(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

# cumulative sums, nothing special
pref = [0]*(n+1)
for i in range(n):
    pref[i+1] = pref[i] + a[i]

# now compute difference array for... whatever reason. Not sure why but let's follow the original.
tmp = []
for i in range(n+1):
    tmp.append(pref[i] - k*i)

# coordinate compress (rust style would be easier for this)
sort_tmp = sorted(set(tmp))
mp = {}
for idx, val in enumerate(sort_tmp):
    mp[val] = idx+1  # making it 1-indexed, annoying but necessary

compact = []
for y in tmp:
    compact.append(mp[y])

answer = 0
bit = BIT(len(sort_tmp))
for x in compact:
    answer += bit.getsum(x)
    bit.add(x, 1)
print(answer)