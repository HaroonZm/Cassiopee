def main():
    # 100*1.01^4000 = 1.9297237e+19
    X = int(input())
    val = 100
    for i in range(4000):
        val = (val * 101) // 100
        if val >= X:
            print(i + 1)
            return

main()