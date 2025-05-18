S = input()
T = input()
flag=1
for i in range(len(S)):
    if S==T:
        flag=0
        print("Yes")
        break
    S = S[-1]+S[:-1]
    # print(S)
    
if flag==1:
    print("No")