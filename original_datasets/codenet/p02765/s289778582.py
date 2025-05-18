n,r = (int(x) for x in input().split())
if n > 10:
    R = r
else:
    R = r + 100*(10-n)

print(R)