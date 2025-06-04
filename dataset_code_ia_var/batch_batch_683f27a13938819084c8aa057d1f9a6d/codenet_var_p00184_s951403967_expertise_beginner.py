import sys

def main():
    while True:
        n = int(input())
        if n == 0:
            break

        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        cnt5 = 0
        cnt6plus = 0

        for i in range(n):
            age = int(input())
            if age < 10:
                cnt0 += 1
            elif age < 20:
                cnt1 += 1
            elif age < 30:
                cnt2 += 1
            elif age < 40:
                cnt3 += 1
            elif age < 50:
                cnt4 += 1
            elif age < 60:
                cnt5 += 1
            else:
                cnt6plus += 1

        print(cnt0)
        print(cnt1)
        print(cnt2)
        print(cnt3)
        print(cnt4)
        print(cnt5)
        print(cnt6plus)

if __name__ == '__main__':
    main()