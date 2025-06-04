val_a, val_b, val_c, val_d = map(int, input().split())
if (val_a == val_b and val_c == val_d) or (val_a == val_c and val_b == val_d) or (val_a == val_d and val_b == val_c):
    print("yes")
else:
    print("no")