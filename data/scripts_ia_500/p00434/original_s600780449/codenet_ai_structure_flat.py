n=[]
for i in range(28):
    n.append(int(input()))
for j in range(1,31):
    if j not in n:
        print(j)