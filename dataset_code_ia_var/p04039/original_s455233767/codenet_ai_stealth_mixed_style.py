import sys

def valid(num, forbidden):
    for c in list(str(num)):
        if c in forbidden: return False
    return True

main = lambda: (
    lambda n,k,d: (
        (lambda seq:
            [(
                print(i), sys.exit()
            ) for i in range(n,10**9) if valid(i, d)]
        )(range(n, 10**9))
    )
)(*map(int, sys.stdin.readline().split()), set(sys.stdin.readline().split()))

if __name__ == "__main__":
    main()