def main():
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    for x in range(len(a)):
        if x == len(a) - 1:
            print(a[x])
        else:
            print(a[x], end = " ")
if __name__ == "__main__":
    main()