from sys import stdin

def get():
    return stdin.readline().rstrip()

A = get()
B = get()
LEN_A = len(A)
LEN_B = len(B)

def verify():
    idx = 0
    while idx <= LEN_A - LEN_B:
        k = 0
        match = True
        while k < LEN_B:
            if (B[k] != "_") and (A[idx + k] != B[k]):
                match = False
                break
            k += 1
        if match:
            return print("Yes")
        idx += 1
    print("No")
    return None

verify()