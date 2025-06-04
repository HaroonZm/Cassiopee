def run(n, a):
    difference = max(a) - min(a)
    return difference

def main():
    n = int(input())
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
    result = run(n, a)
    print(result)

if __name__ == '__main__':
    main()