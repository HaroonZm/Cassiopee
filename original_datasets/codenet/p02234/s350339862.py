def main():
    """ MAIN """
    DAT = []
    num = int(input())
    for i in range(num):
        x, y = list(map(int,input().split()))
        DAT.append(x)
    DAT.append(y)
    num1 = num + 1
    TBL = [[0] * num1 for i in range(num1)]

    for i in range(0, num1):
        for row in range(num-i):
            col = row + i + 1
            for j in range(row+1,col):
                x = DAT[row] * DAT[j] * DAT[col] + TBL[row][j] + TBL[j][col]
                if TBL[row][col] < 1 or TBL[row][col] > x:
                    TBL[row][col] = x

    print("{}".format(TBL[row][col]))

if __name__ == '__main__':
    main()