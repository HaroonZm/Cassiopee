n = int(input())
a = list(map(int,input().split()))
cnt = 0
ans = ''
st = list()
for x in a:
    while cnt < x:
        ans += '('
        cnt += 1
        st.append(cnt)
    if st[-1] == x:
        st.pop()
        ans += ')'
    else:
        ans = ':('
        break
print(ans)