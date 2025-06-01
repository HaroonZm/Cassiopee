list1=[]

for i in range(6):
    n=int(input())
    list1.append(n)

list2=(list1[4:])  
list1=(list1[:4])

list1.sort()
del list1[0]
list2.sort()
del list2[0]

sum1=sum(list1)

sum2=sum(list2)
print(sum1+sum2)