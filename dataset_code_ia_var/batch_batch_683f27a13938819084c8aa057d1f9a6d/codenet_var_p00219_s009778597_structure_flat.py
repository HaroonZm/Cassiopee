while True:
    n = int(input())
    if n == 0:
        break
    a = []
    i = 0
    while i < n:
        a.append(int(input()))
        i += 1
    nums = [0] * 10
    j = 0
    while j < len(a):
        k = int(a[j])
        nums[k] += 1
        j += 1
    t = 0
    while t < 10:
        s = nums[t]
        if s == 0:
            print('-')
        else:
            print('*' * s)
        t += 1