from sys import exit as _e

def _triangle():
    N=int(input())
    nums=[*map(int,input().split())];nums.sort()
    if N<=2:
        print(0)
        _e()
    val=0
    for i in range(N-2):
        j=i+1
        while j<N-1:
            for k in range(j+1,N):
                if not (nums[i]==nums[j] or nums[j]==nums[k]):
                    if (lambda x,y,z: x+y>z)(nums[i],nums[j],nums[k]):
                        val=val+1
            j+=1
    print(val)
_triangle()