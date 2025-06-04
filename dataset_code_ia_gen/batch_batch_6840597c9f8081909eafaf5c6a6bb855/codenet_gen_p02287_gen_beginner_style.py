H = int(input())
A = [0] + list(map(int, input().split()))

for i in range(1, H+1):
    line = "node {}: key = {},".format(i, A[i])
    parent = i // 2
    left = 2 * i
    right = 2 * i + 1

    if parent >= 1:
        line += " parent key = {}, ".format(A[parent])

    if left <= H:
        line += "left key = {}, ".format(A[left])

    if right <= H:
        line += "right key = {}, ".format(A[right])

    print(line)