import sys
input=sys.stdin.readline

C,N=map(int,input().split())
image=[list(map(int,list(input().rstrip()))) for _ in range(N)]

def is_symmetric(img):
    half = N//2
    for r in range(half):
        if img[r]!=img[N-1-r]:
            return False
    for r in range(N):
        for c in range(half):
            if img[r][c]!=img[r][N-1-c]:
                return False
    return True

count=0
if is_symmetric(image):
    count+=1

for _ in range(C-1):
    D=int(input())
    for __ in range(D):
        r,c=map(int,input().split())
        r-=1; c-=1
        image[r][c]^=1
    if is_symmetric(image):
        count+=1

print(count)