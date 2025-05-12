def solve(s):
    R = "qwertasdfgzxcvb"
    L = "yuiophjklnm"
    
    n = len(s)
    if n <= 1:
        return 0
    cnt = 0
    for i in range(n-1):
        if s[i] in R and s[i+1] in L:
            cnt += 1
        if s[i] in L and s[i+1] in R:
            cnt += 1
    return cnt

while True:
    s = raw_input()
    if s == "#":
        break
    print solve(s)