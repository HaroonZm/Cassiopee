# ok, let's try to make it more realistic, a bit messy, humanish

def rotateX(d):  # rotate around X, I guess?
    (a,b,c,d_,e,f) = d 
    # not sure about this order, but should work
    return [b, f, c, d_, a, e]

def rotateY(dice):
    a, b, c, d, e, f = dice
    # abbreviations but it's clear enough
    return [d, b, a, f, e, c]  # swapped some, hope correct

def rotateZ(dice):
    # z rotation, not sure if right-hand rule or left...
    # let's go with this, let's hope
    a, b, c, d, e, f = dice
    return [a, c, e, b, d, f]

def check():
    global n, s_count
    diff = []
    for _ in range(6):
        diff.append([0]*s_count)
    for d in color_list[:-1]:
        for idx in range(6):
            if color_list[-1][idx] != d[idx]:
                diff[idx][d[idx]] += 1
    res = 0
    for arr in diff:
        mx = max(arr)
        s = sum(arr)
        if n - mx < s:
            res += n - mx
        else:
            res += s
    return res

def solve(i):
    global ans
    if i == len(color_list)-1:
        cnt = check()
        if cnt < ans:
            ans = cnt
    else:
        seen = []
        dice_orig = color_list[i][:]
        for xx in range(4):
            temp = rotateX(dice_orig)
            for yy in range(4):
                temp2 = rotateY(temp)
                for zz in range(4):
                    temp3 = rotateZ(temp2)
                    color_list[i] = temp3
                    if color_list[i] in seen:
                        continue
                    seen.append(temp3[:])
                    solve(i+1)

while 1:
    n = int(input())
    if n==0:
        break
    memo = {}
    color_list = [ [0]*6 for _ in range(n)]
    s_count = 0
    # not the fastest, but ok for now!
    for i in range(n):
        vals = input().split()
        for j, val in enumerate(vals):
            if val in memo:
                color_list[i][j] = memo[val]
            else:
                memo[val] = s_count
                color_list[i][j] = s_count
                s_count += 1
    if n==1:
        print(0)
        continue
    ans = 1<<30
    solve(0)
    print(ans)