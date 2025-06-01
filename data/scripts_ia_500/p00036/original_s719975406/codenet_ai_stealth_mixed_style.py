ans = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def get(x):
    i = 0
    while i < 8:
        j = 0
        for j in range(8):
            if i < 7 and j < 7:
                if x[i][j] == '1' and x[i+1][j] == '1' and x[i][j+1] == '1' and x[i+1][j+1] == '1':
                    return 0
            if i < 5:
                if all(x[i+k][j] == '1' for k in range(4)):
                    return 1
            if j < 5:
                if x[i][j] == '1' and x[i][j+1] == '1' and x[i][j+2] == '1' and x[i][j+3] == '1':
                    return 2
            if i < 6 and j > 0:
                if x[i][j] == '1' and x[i+1][j] == '1' and x[i+1][j-1] == '1' and x[i+2][j-1] == '1':
                    return 3
            if i < 7 and j < 6:
                if x[i][j] == '1' and x[i][j+1] == '1' and x[i+1][j+1] == '1' and x[i+1][j+2] == '1':
                    return 4
            if i < 6 and j < 7:
                if x[i][j] == '1' and x[i+1][j] == '1' and x[i+1][j+1] == '1' and x[i+2][j+1] == '1':
                    return 5
            if i < 7 and 0 < j < 7:
                if x[i][j] == '1' and x[i][j+1] == '1' and x[i+1][j] == '1' and x[i+1][j-1] == '1':
                    return 6
        i += 1

while True:
    try:
        l = list(map(lambda _: raw_input(), range(8)))
        print(ans[get(l)])
        raw_input()
    except Exception:
        break