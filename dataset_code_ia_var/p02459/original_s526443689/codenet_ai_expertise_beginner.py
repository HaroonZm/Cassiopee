def main():
    q = int(input())
    d = {}

    for i in range(q):
        para = input().split()

        if para[0] == "0":
            d[para[1]] = int(para[2])
        elif para[0] == "1":
            if para[1] in d:
                print(d[para[1]])
            else:
                print(0)

main()