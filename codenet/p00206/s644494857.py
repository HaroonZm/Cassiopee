def algorithm():
    while True:
        budget = int(input())
        if budget == 0:
            break

        total, months = 0, 0
        for _ in range(12):
            income, outcome = map(int, input().split())
            total += income - outcome
            if total >= budget and months == 0:
                months = _ + 1

        print('NA' if total < budget else months)

def main():
    algorithm()

if __name__ == '__main__':
    main()