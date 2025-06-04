key_list=[]
page_list=[]
while True:
    try:
        key,page=map(str,input().split())
        if key in key_list:
            page_list[key_list.index(key)].append(int(page))
        else:
            key_list.append(key)
            page_list.append([int(page)])
    except:
        break
key_list_sort=sorted(key_list)
for i in key_list_sort:
    print(i)
    ans=sorted(page_list[key_list.index(i)])
    print(' '.join(map(str,ans)))