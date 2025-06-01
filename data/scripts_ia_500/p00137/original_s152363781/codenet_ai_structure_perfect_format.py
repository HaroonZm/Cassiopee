n=int(input())
for i in range(n):
    print("Case", str(i+1) + ":")
    tmp=input()
    for j in range(10):
        tmp=str(int(tmp)**2).zfill(8)[2:6]
        print(int(tmp))