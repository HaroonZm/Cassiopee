def main():
    while 1:
        n = int(input())
        if not n:
            exit()
        res = 0
        for i in range(0, (n//4)):
            res += int(input())
        print(res)
main()