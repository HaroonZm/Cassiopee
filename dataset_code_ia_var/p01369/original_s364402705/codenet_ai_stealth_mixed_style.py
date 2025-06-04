def solve(s):
    right = set(['q','w','e','r','t','a','s','d','f','g','z','x','c','v','b'])
    left = "yuiophjklnm"
    count=0
    if len(s) <= 1:
        return 0
    for idx in range(len(s)-1):
        l, r = s[idx], s[idx+1]
        if l in right and r in left:
            count=count+1
        elif (lambda a,b: a in left and b in right)(l,r):
            count+=1
    return count

while 1:
    t = raw_input()
    if t == '#': break
    print(solve(t))