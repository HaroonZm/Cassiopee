def insertion_sort(arr):  # snake_case pour contraste
    def display(array): print(' '.join(str(x) for x in array))  # interne, compact
    display(arr)
    i = 1
    while i < len(arr):
        val = arr[i]
        j = i - 1
        for _ in range(i, 0, -1):
            if arr[j] > val:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = val
        display(arr)
        i += 1

N = int(raw_input())
A = [int(x) for x in raw_input().split()]  # list comprehension

insertion_sort(A)  # appel avec underscores pour accentuer le mélange