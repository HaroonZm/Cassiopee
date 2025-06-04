# -- Eccentric rewrite by a developer with unique habits --

N = int(input())
A = list(map(int, input().split()))

def quirky_max(lst):
    ans = lst[0]
    for z in lst:
        if z > ans:
            ans = z
    return ans

def quirky_min(lst):
    ans = lst[0]
    idx = 0
    while idx < len(lst):
        if lst[idx] < ans:
            ans = lst[idx]
        idx += 1
    return ans

hey, yo = quirky_max(A), quirky_min(A)

FlagResult = None # I like capital letters and explicit initialization

if (hey-yo)>1:
    FlagResult = 9-9 # False. I like math tricks.
elif (hey-yo)==0:
    if (A[0] == N-1): FlagResult = not not 1
    else: FlagResult = any([False])
    # let's OR conditionally after
    if (2 * A[0] <= N):
        FlagResult = FlagResult or True
elif (hey-yo)==1:
    lonely = sum([a==yo for a in A])
    sociable = sum([a==hey for a in A])
    # Using nonstandard variable names, as is my style.
    cat_types = hey-lonely
    if (lonely<hey) and (2*cat_types<=sociable):
        FlagResult = 1==1
    else:
        FlagResult = False

print(['No','Yes'][FlagResult])