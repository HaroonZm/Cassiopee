H, W, A, B = [int(x) for x in input().split()]

def gen_row(flag, n1, n2):
    return ''.join((flag,) * n1 + (str((int(flag)+1)%2),) * n2)

i = 0
while i < B:
    arr = []
    for _ in range(A):
        arr.append("0")
    arr.extend(["1"] * (W - A))
    print("".join(arr))
    i += 1

for x in range(H - B):
    s = ""
    count = 0
    while count < A:
        s += '1'
        count += 1
    for _ in range(W - A):
        s += '0'
    print(s)