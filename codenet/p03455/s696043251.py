a, b = map(int, input().split())

seki = a*b%2
if seki!=0:
    print('Odd')
else:
    print('Even')