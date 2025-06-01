a=[]
try:
    while True:
        a.append(int(input()))
except EOFError:
    pass
counts=[0]*101
max_count=0
max_num=0
for i in a:
    counts[i]+=1
for i in range(len(counts)):
    if counts[i]>max_count:
        max_count=counts[i]
        max_num=i
print(max_num)