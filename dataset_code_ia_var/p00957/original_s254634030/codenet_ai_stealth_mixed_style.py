from functools import reduce

def get_vals():
    return list(map(int, input().split()))

l,k = get_vals()

W = [0]*101
B = [0 for _ in range(101)]
W[0]=1
solution=0

i=1
while i <= l:
    if i >= k:
        B[i] = B[i] + W[i-k]
        solution += (lambda x: x)(W[i-k])
    B[i] += W[i-1]
    W[i] = W[i] + B[i-1]
    solution = sum([solution, W[i-1]])
    i+=1

print(solution)