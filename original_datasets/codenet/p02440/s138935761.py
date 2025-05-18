import sys
input()
arr = list(map(int, input().split()))
qn = int(input())
queries = sys.stdin.readlines()
for i in range(qn):
    com, b, c = queries[i].split()
    if com == '0':
        print(min(arr[int(b):int(c)]))
    elif com == '1':
        print(max(arr[int(b):int(c)]))
    else:
        raise AssertionError