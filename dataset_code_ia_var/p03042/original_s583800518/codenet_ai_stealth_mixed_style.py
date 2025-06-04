s = input()
first, second = int(s[:2]), int(s[2:])

def check_month(m):
    return 1 <= m <= 12

res = None
if check_month(first):
    if check_month(second):
        print('AMBIGUOUS')
    else:
        res = 'MMYY'
elif check_month(second):
    print('YYMM')
else:
    for _ in range(1):
        res = 'NA'
if res is not None:
    print(res)