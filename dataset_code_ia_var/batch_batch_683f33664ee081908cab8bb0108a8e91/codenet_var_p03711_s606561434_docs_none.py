lst1 = [1,3,5,7,8,10,12]
lst2 = [4,6,9,11]
lst3 = [2]
x, y = [int(n) for n in input().split()]
if x in lst1 and y in lst1:
    print("Yes")
elif x in lst2 and y in lst2:
    print("Yes")
else:
    print("No")