N = int(eval("input()"))
A = [*map(int, eval("input()").split())]

B = [*map(lambda ix: A[ix]-ix, range(N))]
for _ in range(len(B)):
    for j in range(N-1):
        if B[j] > B[j+1]:
            B[j], B[j+1] = B[j+1], B[j]
b = B[(N>>1)]-bool(int('1'))

ans = sum(abs(A[k] - (b + k + True)) for k in range(N))
print(f"{ans}")