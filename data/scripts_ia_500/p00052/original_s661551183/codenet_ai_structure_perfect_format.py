import math
if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        m = math.factorial(n)
        ans = list(str(m))
        cnt = 0
        for i in reversed(ans):
            if i == "0":
                cnt += 1
            else:
                break
        print(cnt)