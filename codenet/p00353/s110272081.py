m, f ,b = map(int, input().split())
lending = max(b - m, 0)
if lending <= f:
    print(lending)
else:
    print("NA")