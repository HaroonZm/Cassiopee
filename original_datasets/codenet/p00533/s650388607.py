h,w = map(int, input().split())
for _ in range(h):
    s = input()
    ans = []
    for i in range(len(s)):
        if s[i] == 'c':
            ans.append(0)
        elif i == 0:
            ans.append(-1)
        else:
            for j in range(1,i+1):
                if s[i-j] == 'c':
                    ans.append(j)
                    break
                if j == i:
                    ans.append(-1)
    print(' '.join(map(str, ans)))