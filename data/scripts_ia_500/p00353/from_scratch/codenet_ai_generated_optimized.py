m, f, b = map(int, input().split())
diff = b - m
if diff <= 0:
    print(0)
elif diff <= f:
    print(diff)
else:
    print("NA")