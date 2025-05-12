N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
AandB = sorted(A & B)
AorB = sorted(A | B)
print(len(AandB), len(AorB))
for x in AandB:
    print(x)
for x in AorB:
    print(x)