n = int(input())
A = list(map(int, input().split()))
m = int(input())
for i in range(m):
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    size = b - a
    temp1 = A[a:b]
    temp2 = A[c:c+size]
    for j in range(size):
        A[a+j] = temp2[j]
        A[c+j] = temp1[j]
print(' '.join(str(x) for x in A))