def main():
    while(True):
        N, M = map(int, input().split())
        if(N == 0 and M == 0):
            return
        skc = []
        for i in range(M):
            skc.append(list(map(int, input().split())))
        point = [0 for i in range(N)]
        for i in range(M):
            for j in range(2, len(skc[i])):
                point[skc[i][j] - 1] += skc[i][0]
        point_fixed = [0 for i in range(N)]
        for i in range(M):
            if(skc[i][1] == 1):
                point_fixed[skc[i][2] - 1] += skc[i][0]
        maxPlayer = 0
        Max = 0
        for i in range(N):
            if(Max < point[i]):
                Max = point[i]
                maxPlayer = i + 1
        minPlayer = 0
        Min = 1e9
        for i in range(N):
            if(i + 1 == maxPlayer):
                continue
            if(Min > point_fixed[i]):
                Min = point_fixed[i]
                minPlayer = i + 1        
        print(point[maxPlayer - 1] - point_fixed[minPlayer - 1] + 1)

if __name__ == '__main__':
    main()