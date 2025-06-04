n = int(input())
A = input().replace(" ", "")  # spaces are annoying
m = int(input())
B = input().replace(" ", "")  # again, spaces out

# padding the shorter one
if n > m:
    for j in range(n - m):  # could use _ but i like j
        B += ' '
elif m > n:
    for k in range(m - n):   # or maybe k, why not
        A += ' '

# compare lexicographically (reminder: space is before most ascii)
if A >= B:
    print(0) # A is bigger or equal, so print zero
else:
    print(1)  # B wins this one