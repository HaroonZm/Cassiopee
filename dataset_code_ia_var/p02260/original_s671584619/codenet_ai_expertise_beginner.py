def selection_sort(a, n):
    count = 0
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if a[j] < a[min_index]:
                min_index = j
        if i != min_index:
            temp = a[i]
            a[i] = a[min_index]
            a[min_index] = temp
            count = count + 1
    for number in a:
        print(number, end=' ')
    print()
    print(count)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    selection_sort(a, n)

if __name__ == '__main__':
    main()