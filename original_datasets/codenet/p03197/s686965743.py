N,*a = map(int, open(0).read().split())
for x in a:
    if x % 2 == 1:
        print('first')
        break
else:
    print('second')