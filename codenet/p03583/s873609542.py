def main():
    N = int(input())

    h, n, w = -1, -1, -1
    for i in range(1, 3501):
        for j in range(i, 3501):
            if 4*i*j > N*i+N*j:
                if N*i*j % (4*i*j-N*i-N*j) == 0:
                    h, n = i, j
                    w = N*i*j // (4*i*j-N*i-N*j)
                    break

        else:
            continue
        break

    print(h, n, w)

if __name__ == '__main__':
    main()