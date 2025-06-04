import sys

def age_distribution(ages):
    counts = [0]*7
    for age in ages:
        if age < 10:
            counts[0] += 1
        elif age < 20:
            counts[1] += 1
        elif age < 30:
            counts[2] += 1
        elif age < 40:
            counts[3] += 1
        elif age < 50:
            counts[4] += 1
        elif age < 60:
            counts[5] += 1
        else:
            counts[6] += 1
    return counts

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        ages = [int(input()) for _ in range(n)]
        result = age_distribution(ages)
        for count in result:
            print(count)

if __name__ == "__main__":
    main()