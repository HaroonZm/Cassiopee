N = int(input())
for i in range(N):
    bolls = list(map(int, input().split(' ')))
    left = [-1]
    right = [-1]
    possible = False
    stack = [ (left, right, bolls) ]
    while stack:
        l, r, rem = stack.pop()
        if len(rem) == 0:
            possible = True
            break
        boll = rem[0]
        if boll > max(l):
            stack.append( (l + [boll], r, rem[1:]) )
        if boll > max(r):
            stack.append( (l, r + [boll], rem[1:]) )
    if possible:
        print('YES')
    else:
        print('NO')