N_M = input().split()
N = int(N_M[0])
M = int(N_M[1])
A_list = input().split()
A = set()
for x in A_list:
    A.add(int(x))
B_list = input().split()
B = set()
for x in B_list:
    B.add(int(x))
AandB = []
for x in A:
    if x in B:
        AandB.append(x)
AandB.sort()
AorB = []
for x in A:
    if x not in AorB:
        AorB.append(x)
for x in B:
    if x not in AorB:
        AorB.append(x)
AorB.sort()
print(len(AandB), len(AorB))
for x in AandB:
    print(x)
for x in AorB:
    print(x)