A, *b = [int(x) for x in input().split()]
q, r = divmod(A, b[0])
X = sum([q, r])
print(f"{X}")