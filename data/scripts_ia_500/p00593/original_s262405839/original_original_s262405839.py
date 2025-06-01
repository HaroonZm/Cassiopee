if __name__ == '__main__':
    TC = 1
    while True:
        N = int(input())
        if N == 0:
            break

        arr = [ [ 0 for _ in range(N) ] for _ in range(N) ]

        i = 0
        j = 0
        val = 1
        prevMove = "UR"

        while True:
            arr[i][j] = val
            val += 1

            if i == N - 1 and j == N - 1:
                break
            elif i == 0:
                if prevMove == "UR":
                    if j != N - 1:
                        j += 1
                        prevMove = "R"
                    else:
                        i += 1
                        prevMove = "D"
                else:
                    i += 1
                    j -= 1
                    prevMove = "DL"
            elif i == N - 1:
                if prevMove == "DL":
                    j += 1
                    prevMove = "R"
                else:
                    i -= 1
                    j += 1
                    prevMove = "UR"
            elif j == 0:
                if prevMove == "DL":
                    i += 1
                    prevMove = "D"
                else:
                    i -= 1
                    j += 1
                    prevMove = "UR"
            elif j == N - 1:
                if prevMove == "UR":
                    i += 1
                    prevMove = "D"
                else:
                    i += 1
                    j -= 1
                    prevMove = "DL"
            else:
                if prevMove == "DL":
                    i += 1
                    j -= 1
                else:
                    i -= 1
                    j += 1

        print("Case {}:".format(TC))
        TC += 1

        for i in range(N):
            for j in range(N):
                print("{:3d}".format(arr[i][j]), end='')
            print()