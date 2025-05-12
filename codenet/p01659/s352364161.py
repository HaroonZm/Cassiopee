input()
ans = 0
st = [0]
for a in map(int, raw_input().split()):
    while a<st[-1]:
        st.pop(); ans += 1
    if st[-1] < a: st.append(a)
print ans+len(st)-1