def main():
    A, B = map(int, input().split())
    S = input()
    cond = [
        len(S) == A + B + 1,
        S[A] == '-',
        S[:A].isdigit(),
        S[A + 1:].isdigit()
    ]
    print('Yes' if all(cond) else 'No')

if __name__ == '__main__':
    main()