# AOJ ITP1_10_C

import math

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def main():
    while True:
        n = int(input())
        if n == 0: break
        data = intinput()
        sum_1 = 0  # 1乗の総和
        sum_2 = 0  # 2乗の総和
        for i in range(n):
            sum_1 += data[i]; sum_2 += data[i] ** 2
        # print('(%d, %d)' % (sum_1, sum_2))
        sigma = math.sqrt((sum_2 / n) - ((sum_1 / n) ** 2))
        print(sigma)

if __name__ == "__main__":
    main()