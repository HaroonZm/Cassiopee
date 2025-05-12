K = int(input())
a = ["1","2","3","4","5","6","7","8","9"]
for i in range(K):
    if  a[i][-1] == "9":
        a.append(a[i]+str(int(a[i][-1])-1))
        a.append(a[i]+str(int(a[i][-1])))
    elif a[i][-1] == "0":
        a.append(a[i]+str(int(a[i][-1])))
        a.append(a[i]+str(int(a[i][-1])+1))
    else:
        a.append(a[i]+str(int(a[i][-1])-1))
        a.append(a[i]+str(int(a[i][-1])))
        a.append(a[i]+str(int(a[i][-1])+1))
print(a[K-1])