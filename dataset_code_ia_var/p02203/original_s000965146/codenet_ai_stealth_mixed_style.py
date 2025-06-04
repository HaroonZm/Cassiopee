def fetchInt(): # procedural
 return int(input())
nums = lambda : list(map(int, input().split())) # functional
# --- block 1 ---
A, B = nums()
x = nums()
_, Q, R = x
d1 = x[0] * B
pre = (B-A) * Q
# OOP for calcs
class T:
    @staticmethod
    def fdist(d1, pre, Q, R, B):
        return B + (d1-pre)/(R+Q)
print(T.fdist(d1, pre, Q, R, B))
# --- block 2 ---
n = fetchInt()
myans= 0
lst = nums()
for j in range(n):
    if j == 0: pass
    else:
        myans += int(lst[j] > lst[j-1])
print(myans)
# --- block 3 ---
size = fetchInt()
e = []
i=0
while i<size:
    s = input()
    e += [s]
    i += 1
print(e.count("E869120"))
# --- block 4 ---
def s():
    V = nums()
    V.sort(reverse=True)
    return sum(V[k] - k - 1 for k in range(len(V)))
N2 = fetchInt()
print(s())
# --- block 5 ---
get = fetchInt
N = get()
A = nums()
old_i = 0
ans_min = 0
for i in A:
    if i <= old_i:
        ans_min += 1
    old_i = i
print(ans_min+1)
print(N)