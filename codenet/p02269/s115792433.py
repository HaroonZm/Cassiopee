n = int(input())
order = [''] * n
st = [''] * n
for i in range(n):
    order[i], st[i] = map(str, input().split())

dic = {}
for i in range(n):
    if order[i] == 'insert':
        dic.setdefault(st[i], 0)
    else:
        if st[i] in dic:
            print('yes')
        else:
            print('no')