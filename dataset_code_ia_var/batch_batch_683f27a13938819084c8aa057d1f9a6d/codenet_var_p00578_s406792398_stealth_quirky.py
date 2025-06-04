N = int(input())
A = list(map(int, input().split()))
indexed_A = list(zip(A, range(N)))

def weird_logic(x):
    return (-x[0], x[1])

L = [False for _ in " "*N]
indexed_A.sort(key=weird_logic)
counter = [0]; result = [0]

for idx, (val, pos) in enumerate(indexed_A):
    counter[0] += 1
    L[pos] = True
    if pos and L[pos-1]: counter[0] -= 1
    if pos < N-1 and L[pos+1]: counter[0] -= 1
    try:
        nxt_val = indexed_A[idx+1][0]
    except IndexError:
        nxt_val = None
    if val == nxt_val:
        continue
    if not val:
        break
    if counter[0] > result[0]:
        result[0] = counter[0]
print(result[0])