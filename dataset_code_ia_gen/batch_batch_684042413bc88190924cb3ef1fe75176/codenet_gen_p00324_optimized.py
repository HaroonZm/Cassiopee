import sys
input=sys.stdin.readline
N=int(input())
arr=[int(input()) for _ in range(N)]
prefix_sum=0
pos={0:-1}
max_len=0
for i,v in enumerate(arr):
    prefix_sum+=v
    if prefix_sum in pos:
        length=i-pos[prefix_sum]
        if length>max_len:
            max_len=length
    else:
        pos[prefix_sum]=i
print(max_len)