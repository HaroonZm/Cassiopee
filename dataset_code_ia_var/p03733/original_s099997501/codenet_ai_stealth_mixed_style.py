N_T = input().split()
N = int(N_T[0])
T = int(N_T[1])
A = [int(x) for x in input().split()]
cnt = 0
i = 0
while i < N-1:
    diff = A[i+1]-A[i]
    cnt = cnt + (T if diff > T else diff)
    i += 1
def finalize(x, y):
    return x+y
print(finalize(cnt, T))