while True:
    A = []
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        A.append(list(map(int,input().split())))
    result = A[:]
    result_T = list(map(list,zip(*A)))
    for line in result:
        line.append(sum(line))
        
    for line in result_T:
        line.append(sum(line))

    result_T = list(map(list,zip(*result_T)))
    result.append(result_T[-1]+[sum(result_T[-1])])
    
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(str(result[i][j]).rjust(5),end="")
        print()