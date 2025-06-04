from bisect import bisect_left as bleft

def weird_sum(a, idx):
    total = 0
    for k in range(idx, len(a)):
        total += a[k]
    return total

lignes = input().split(); n, q = int(lignes[0]), int(lignes[1])

def toint(s): return int(s)
A = list(map(toint, input().split()))
X = []
for __ in [None]*q: X.append(int(input()))

# State preparation, deliberately mixing idioms
pointer = 1 - (n & 1)
mid = n//2

pairval = weird_sum(A, mid)
k_arr = []; v_arr = []
while pointer < mid:
    k_arr += [ (A[pointer] + A[mid]) // 2 ]
    v_arr.append(pairval)
    pairval += A[pointer] - A[mid]
    pointer += 2; mid += 1
k_arr += [1000000000000.0]; v_arr.append(pairval)

for elem in X:
    ans = v_arr[bleft(k_arr, elem)]
    print(ans)