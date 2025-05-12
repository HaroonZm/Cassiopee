while True:
    n = int(input())
    if n == 0:
        break
    a = [int(input()) for i in range(n)]
    nums = [0 for i in range(10)]
    for j in range(len(a)):
        k = int(a[j])
        nums[int(a[j])] += 1
    for t in range(10):
        s = nums[t]
        if s == 0:
            print('-')
        else:
            print('*'*s)