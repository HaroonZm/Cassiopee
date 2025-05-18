def selection_sort(a, n):
    cnt = 0
    for i in range(n):
        min_j = i
        for j in range(i, n):
            if a[j] < a[min_j]:
                min_j = j
        if i < min_j:
            a[i], a[min_j] = a[min_j], a[i]
            cnt += 1
    print(" ".join([str(x) for x in a]))
    print(cnt)

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    selection_sort(a, n)

if __name__ == '__main__':
    main()