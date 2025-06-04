def main():
    while True:
        n = int(input())
        if n == 0:
            break

        under10 = 0
        age10s = 0
        age20s = 0
        age30s = 0
        age40s = 0
        age50s = 0
        age60s = 0

        for i in range(n):
            age = int(input())
            if age < 10:
                under10 += 1
            elif age < 20:
                age10s += 1
            elif age < 30:
                age20s += 1
            elif age < 40:
                age30s += 1
            elif age < 50:
                age40s += 1
            elif age < 60:
                age50s += 1
            else:
                age60s += 1

        print(under10)
        print(age10s)
        print(age20s)
        print(age30s)
        print(age40s)
        print(age50s)
        print(age60s)

main()