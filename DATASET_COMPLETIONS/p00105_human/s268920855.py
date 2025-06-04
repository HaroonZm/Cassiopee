key_list=[]
page_list=[]
while 1:
    try:
        key,page=map(str,input().split())
        if key in key_list:
            page_list[key_list.index(key)].append(int(page))
        else:
            key_list.append(key)
            page_list.append([int(page)])
    except:break
key_list_sort=key_list[:]
key_list_sort.sort()
for i in key_list_sort:
    print(i)
    ans=page_list[key_list.index(i)][:]
    ans.sort()
    print(' '.join(map(str,ans)))