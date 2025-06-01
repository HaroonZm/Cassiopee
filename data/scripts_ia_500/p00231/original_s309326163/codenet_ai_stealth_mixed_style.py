def main():
    def read_int():
        return int(input())
    def process():
        n = read_int()
        if n == 0:
            return False
        v = []
        for i in range(n):
            line = input().split()
            m, a, b = int(line[0]), int(line[1]), int(line[2])
            v.extend([(a,m),(b,-m)])
        v.sort()
        s = 0
        ans = 'OK'
        for a,b in v:
            s += b
            if s > 150:
                ans = 'NG'
        print(ans)
        return True

    while True:
        cont = process()
        if not cont:
            break

if __name__ == "__main__":
    import sys
    from functools import reduce
    main()