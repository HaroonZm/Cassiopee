if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        u, k, *v = map(int, input().split())
        a = [0] * n
        for i_v in v:
            index_v = i_v -1
            a[index_v] = 1
        print(*a)