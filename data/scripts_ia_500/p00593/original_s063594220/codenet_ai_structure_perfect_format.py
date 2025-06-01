otehon=[[1,2,6,7,15,16,28,29,45],[3,5,8,14,17,27,30,44],[4,9,13,18,26,31,43],[10,12,19,25,32,42],[11,20,24,33,41],[21,23,34,40],[22,35,39],[36,38],[37]]

def xyz(num):
    num = str(num)
    if len(num) == 1:
        return "  "+num
    return " "+num

n = 0
while True:
    N = int(raw_input())
    if N == 0:
        break
    n += 1
    hairetu = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if i + j < N:
                hairetu[i][j] = otehon[i][j]
    for i in range(N):
        for j in range(N):
            if i + j >= N:
                hairetu[i][j] = N * N + 1 - hairetu[N - 1 - i][N - 1 - j]
    print "Case "+str(n)+":"
    for i in range(N):
        strn = ""
        for j in range(N):
            strn += xyz(hairetu[i][j])
        print strn