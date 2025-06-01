def algorithm():
    budget = int(input())
    while budget != 0:
        total = 0
        months = None
        for i in range(12):
            income, outcome = list(map(int, input().split()))
            total = total + (income - outcome)
            if months is None and total >= budget:
                months = i+1

        if total < budget:
            print("NA")
        else:
            print(months)

        budget = int(input())

def main():
    algorithm()

if __name__ == '__main__':
    main()