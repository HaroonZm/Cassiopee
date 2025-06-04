n = int(input())
a = list(map(int, input().split()))
cnt = 0
ans = ''
st = []
i = 0
while i < n:
    x = a[i]
    while cnt < x:
        ans += '('
        cnt += 1
        st.append(cnt)
    if len(st) > 0 and st[-1] == x:
        st.pop()
        ans += ')'
    else:
        ans = ':('
        break
    i += 1
print(ans)