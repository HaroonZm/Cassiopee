def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

first = True
while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    if not first:
        print()
    first = False
    res = [str(y) for y in range(a,b+1) if is_leap_year(y)]
    if res:
        print('\n'.join(res))
    else:
        print("NA")