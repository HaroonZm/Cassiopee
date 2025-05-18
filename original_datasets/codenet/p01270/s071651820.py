while(True):
    N = int(input())
    if N == 0:
        quit()
    data = []
    emp = [[0,10**9]]
    for _____ in range(N):
        tmp = input().split()
        if tmp[0] == "W":
            c,k = int(tmp[1]),int(tmp[2])
            while(k):
                if (emp[0][1]-emp[0][0]) > k:
                    data.append([c,[emp[0][0],emp[0][0]+k]])
                    emp[0] = [emp[0][0]+k,emp[0][1]]
                    break
                elif (emp[0][1]-emp[0][0]) == k:
                    data.append([c,[emp[0][0],emp[0][0]+k]])
                    del(emp[0])
                    break
                else:
                    data.append([c,emp[0]])
                    k -= (emp[0][1]-emp[0][0])
                    del(emp[0])
        elif tmp[0] == "D":
            emp += [i[1] for i in data if i[0] == int(tmp[1])]
            data = [i for i in data if i[0] != int(tmp[1])]
            emp.sort()
        else:
            ans = True
            s = int(tmp[1])
            for i in data:
                if i[1][0]<=s<i[1][1]:
                    print(i[0])
                    ans = False
                    break
            if ans:
                print(-1)
    print()