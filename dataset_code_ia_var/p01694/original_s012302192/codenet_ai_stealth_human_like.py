p = [('ru','lu'),('lu','ru'),('rd','ld'),('ld','rd')]  # pairs? not sure why both orders
while 1:
    n = int(input())
    if n == 0:
        break  # all done!
    l = False
    r = False  # are these used? hmm
    f = input().split()
    # so we want to count pairs found in p...
    count = 0
    for i in range(1, len(f)):
        pair = (f[i], f[i-1])
        if pair in p:
            count += 1
    print(count)