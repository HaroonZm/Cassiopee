n = int(input())
T, A = (int(x) for x in input().split())
H = list(map(int, input().split()))
differences = []
for idx in range(len(H)):
    v = T - H[idx] * 0.006
    differences.append(abs(v - A))
indices = [i+1 for i, val in enumerate(differences) if val == min(differences)]
if len(indices):
    print(indices[0])
else:
    print(1)