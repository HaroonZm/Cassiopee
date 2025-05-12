time=int(input())
nums=[int(i) for i in input().split()]
odd=0
even=0
even35=0
for j in range(time):
    if nums[j]%2==0:
        even+=1
        if nums[j]%3!=0 and nums[j]%5!=0:
            continue
        else:
            even35+=1
    else:
        odd+=1
        
if even35==even:
    print("APPROVED")
else:
    print("DENIED")