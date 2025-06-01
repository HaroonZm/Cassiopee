def checker(a):
    if any([a[0]<a[4]>a[2], a[0]>a[6]<a[2], a[1]<a[5]>a[3], a[1]>a[7]<a[3]]):
        return 'NO'
    else:
        return 'YES'

while True:
    try:
        line = input()
        a = list(map(lambda x: float(x), line.split()))
        print(checker(a))
    except EOFError:
        break