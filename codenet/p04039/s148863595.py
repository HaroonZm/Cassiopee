#!python

def main():
    N, K = input().split(' ')
    D = set(map(int, input().split(' ')))
    can_use_num = set(map(str, set(range(10)) - D))

    n = int(N)
    while True:
        if set(str(n)) <= can_use_num:
            break
        n += 1
    print(n)

if __name__ == '__main__':
    main()