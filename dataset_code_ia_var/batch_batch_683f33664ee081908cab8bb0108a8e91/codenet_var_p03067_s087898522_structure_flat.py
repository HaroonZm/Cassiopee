A, B, C = [int(_) for _ in input().split()]
lst = [A, B, C]
lst_sorted = sorted(lst)
if lst_sorted[1] == C:
    print("Yes")
else:
    print("No")