def split_vals(string):
    return [int(x) for x in string.strip().split()]

def even(num):
    return num % 2 == 0

vals = input()
A,B,K = split_vals(vals)

turn = 1
idx = 0

while idx < K:
    if turn:
        if A & 1:
            A -= 1
        half = A//2
        B = B + half
        A //= 2
        turn = 0
    else:
        if B % 2:
            B = B - 1
        chunk = B//2
        A += chunk
        B = B//2
        turn = 1
    idx += 1

print("{} {}".format(A,B))