def main():
    N = int(input())
    A = list(map(int, input().split()))
    k = len(set(A))

    if k%2 == 1:
        print(k)
    else:
        print(k-1)
            
if __name__ == "__main__":
    main()