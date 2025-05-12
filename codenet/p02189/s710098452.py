def num():
    return int(input())
def nums():
    return list(map(int,input().split()))

N = num()
A = nums()
print(A.index(min(A))+1)