from bisect import bisect

if __name__ == "__main__":
    n = int(input())
    a = list(map(lambda x: int(x), input().split()))
    num_query = int(input())

    for _ in range(num_query):
        k = int(input())
        print(f"{bisect(a, k - 1)} {bisect(a, k)}")