a=input()
for i in range(len(a)):
    if a.count(a[i])%2!=0:
        print('No')
        exit()
print('Yes')