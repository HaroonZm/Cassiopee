from collections import defaultdict

def main():
    q = int(input())
    d = defaultdict(int)

    for _ in range(q):
        para = input().split()

        if para[0] == "0":
            d[para[1]] = int(para[2])

        elif para[0] == "1":
            print(d[para[1]])
main()