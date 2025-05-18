n =int(raw_input())
taro =0
hana =0
for i in range(n):
    a=raw_input().split(" ")
    if(a[0]>a[1]):
        taro +=3
    elif(a[1]>a[0]):
        hana +=3
    else:
        taro +=1
        hana +=1
print taro,hana