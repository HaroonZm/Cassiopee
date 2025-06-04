N, K = (int(x) for x in input().split())
ab = []
i = 0
while i < N:
    a, b = map(int, input().split())
    ab.append([a, b])
    i += 1

def custom_sort(L):
    # insertion sort on first element
    for idx, elem in enumerate(L):
        j = idx
        while j > 0 and L[j-1][0] > L[j][0]:
            L[j-1], L[j] = L[j], L[j-1]
            j -= 1
    return L

ab = custom_sort(ab)

summed = 0
for index in range(len(ab)):
    summed = summed + ab[index][1]
    if K <= summed:
        print(ab[index][0]); exit()