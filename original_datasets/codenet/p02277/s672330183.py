import copy

def partition(p, r):
    i = p
    for j in range(p, r):
        if A[r][1] >= A[j][1]:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[r], A[i] = A[i], A[r]
    return i

def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)

def correct_same_num_suits(l, num, first):
    suits = []
    for i in range(first, N):
        if num == l[i][1]:
            suits.append(l[i][0])
    return suits

def is_stable():
    idx = 0
    while idx < N-1:
        idx_incr_flg = True
        if A[idx][1] == A[idx+1][1]:
            num = A[idx][1]
            sorted_suits = correct_same_num_suits(A, num, idx)
            orig_suits = correct_same_num_suits(orig_list, num, 0)
            if sorted_suits != orig_suits:
                return False
            idx += len(sorted_suits)
            idx_incr_flg = False
        if idx_incr_flg:
            idx += 1
    return True

N = int(input())
A = []
for _ in range(N):
    suit, num = input().split()
    num = int(num)
    A.append([suit, num])
orig_list = copy.deepcopy(A)

quick_sort(0, N-1)

is_stable = is_stable()
if is_stable:
    print("Stable")
else:
    print("Not stable")

for card in A:
    print("%s %d" % (card[0], card[1]))