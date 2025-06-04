n = int(input()) + 1
print((n & -n) << ((n & 1) ^ 1))