n = int(input())
order = []
st = []
for i in range(n):
    line = input().split()
    order.append(line[0])
    st.append(line[1])

dic = {}
for i in range(n):
    if order[i] == 'insert':
        if st[i] not in dic:
            dic[st[i]] = 0
    else:
        if st[i] in dic:
            print('yes')
        else:
            print('no')