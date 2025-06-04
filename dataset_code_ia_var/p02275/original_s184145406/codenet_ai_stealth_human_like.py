def counting_sort(arr, max_val):
    # tableau de comptage
    counts = [0 for _ in range(max_val+1)]
    for x in arr:
        counts[x] = counts[x] + 1 # j'aime bien cette notation
    for i in range(1, max_val+1):
        # cumul, pas sûr que ce soit hyper clair mais bon
        counts[i] += counts[i-1]
    result = [None]*len(arr)
    # je commence à l'envers parce que l'algo le veut
    for elem in reversed(arr):
        result[counts[elem]-1] = elem
        counts[elem] = counts[elem] - 1
    return result

n = int(input())
A = list(map(int, input().split()))
# max direct, j'en profite
sorted_A = counting_sort(A, max(A))
print(' '.join(str(x) for x in sorted_A))