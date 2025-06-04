s = input()
n = len(s)
m = 0
pair = {('(',')'),(')','('),('{','}'),('}','{'),('[',']'),(']', '[')}

def is_pair(a,b):
    return (a,b) in pair

def dp(l,r):
    if l>r:
        return 0, False
    if l==r:
        if s[l] in 'iw':
            return 1, True
        return 0, False
    key = (l,r)
    if memo[key]!=-1:
        return memo[key], has_iwi[key]
    res = 0
    have = False
    
    # check whole substring
    # if s[l]==s[r] and inside is palindrome, but only for i,w or matching pairs
    # but since for pair brackets they invert, match is s[l], s[r] in pair
    
    # try to combine s[l] and s[r]
    inner_len, inner_iwi = dp(l+1,r-1)
    if s[l] in 'iw' and s[l]==s[r]:
        if inner_len==(r-l-1) or inner_len==0:
            res = inner_len + 2
            have = inner_iwi or (res>=3 and contains_iwi(l,r))
    elif is_pair(s[l],s[r]):
        if inner_len==(r-l-1) or inner_len==0:
            res = inner_len + 2
            have = inner_iwi or (res>=3 and contains_iwi(l,r))
    # try all partition
    for k in range(l,r):
        left_len, left_iwi = dp(l,k)
        right_len, right_iwi = dp(k+1,r)
        total_len = left_len+right_len
        if total_len>res:
            res=total_len
            have=left_iwi or right_iwi
        elif total_len==res and not have and (left_iwi or right_iwi):
            have=True
    memo[key]=res
    has_iwi[key]=have
    return res, have

# check if s[l:r+1] contains "iwi" as a subsequence
def contains_iwi(l,r):
    seq = ['i','w','i']
    idx = 0
    for i in range(l,r+1):
        if s[i]==seq[idx]:
            idx+=1
            if idx==3:
                return True
    return False

memo = {}
has_iwi = {}
for i in range(n):
    for j in range(n):
        memo[(i,j)] = -1
        has_iwi[(i,j)] = False
length, contain = dp(0,n-1)
if contain:
    print(length)
else:
    print(3)  # minimum "iwi" only possible by picking "iwi" directly, guaranteed by problem constraints