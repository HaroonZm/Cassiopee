m, f, b = map(int, input().split())
print(l := max(b - m, 0)) if l <= f else print("NA")