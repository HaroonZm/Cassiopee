N, M = map(int, input().split())
initial = list(map(int, input().split()))
p = list(map(int, input().split()))

def build_target(p, start_bit):
    target = []
    bit = start_bit
    for length in p:
        target += [bit] * length
        bit = 1 - bit
    return target

def count_swaps(initial, target):
    swaps = 0
    arr = initial[:]
    for i in range(len(arr)):
        if arr[i] != target[i]:
            # find where the correct bit is in arr after position i
            j = i + 1
            while j < len(arr) and arr[j] != target[i]:
                j += 1
            # bubble it to position i
            while j > i:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swaps += 1
                j -= 1
    return swaps

# try both possible starting bits
bit0 = initial[0]
target1 = build_target(p, 0)
target2 = build_target(p, 1)

# check which target is possible (same counts of bits)
from collections import Counter
count_initial = Counter(initial)
count_target1 = Counter(target1)
count_target2 = Counter(target2)

res = -1

if count_initial == count_target1:
    res = count_swaps(initial, target1)
if count_initial == count_target2:
    s = count_swaps(initial, target2)
    if res == -1 or s < res:
        res = s

print(res)