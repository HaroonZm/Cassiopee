a, b, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
qupons = [list(map(int, input().split())) for _ in range(m)]
cand1 = min(A) + min(B)
prices_with_qpons = [A[q[0]-1] + B[q[1]-1] - q[2] for q in qupons]
cand2 = min(prices_with_qpons) if prices_with_qpons else float('inf')
print(min(cand1, cand2))