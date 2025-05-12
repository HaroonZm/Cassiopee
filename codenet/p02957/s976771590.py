def main():
    a, b = [int(x) for x in input().split()]
    if (a+b)%2 == 0:
        k = int((a+b)/2)
        print(k)
    else:
        print('IMPOSSIBLE')

if __name__ == '__main__':
    main()