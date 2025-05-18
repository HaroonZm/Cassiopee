A, B, C = [int(_) for _ in input().split()]

if sorted([A, B, C])[1] == C:
    print("Yes")
else:
    print("No")