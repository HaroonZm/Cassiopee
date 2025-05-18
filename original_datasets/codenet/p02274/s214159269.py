def swap(list,i,j,count):
    if(list[j]<list[i]):
        list[i],list[j]=list[j],list[i]
        count[0]+=1
        return 1
    return 0

def merge(list,left1,left2,right2,count):#ソート済みの２つの区間(list[left1]〜list[left2-1]と、list[left2]〜list[right2-1]）を結合する
    i=left1
    j=left2
    tmp_list=[]
    while(1):
        if(list[i] <=list[j]):
            tmp_list.append(list[i])
            i+=1
        else:
            tmp_list.append(list[j])
            j+=1
            count[0]+=left2-i
        if(i==left2):
            for k in range(j,right2):
                tmp_list.append(list[k])
            break
        if(j==right2):
            for k in range(i,left2):
                tmp_list.append(list[k])
            break
    for k in range(left1,right2):
        list[k]=tmp_list[k-left1]
    

                
                
    
        

def merge_sort(list,left,right,count):#list[left]からlist[right]までの要素でマージソート
    if(right  == left ):
        return None
    if(left+1 == right):
        swap(list,left,right,count)
    else:
        mid=(left + right)//2
        merge_sort(list,left,mid,count)
        merge_sort(list,mid+1,right,count)
        merge(list,left,mid+1,right+1,count)
        

n=int(input())
data=list(map(int,input().split()))
count=[0]
merge_sort(data,0,n-1,count)
print(count[0])