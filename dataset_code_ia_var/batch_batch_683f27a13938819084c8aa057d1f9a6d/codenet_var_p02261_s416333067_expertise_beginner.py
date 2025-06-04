def bubblesort(L, N):
    # On fait une copie de la liste pour ne pas modifier l'originale
    result = []
    for item in L:
        result.append(item)
    # Bulle sort
    for i in range(N):
        j = N - 1
        while j > i:
            if int(result[j][1]) < int(result[j - 1][1]):
                tmp = result[j]
                result[j] = result[j - 1]
                result[j - 1] = tmp
            j = j - 1
    return result

def selectionsort(L, N):
    sorted_list = []
    for item in L:
        sorted_list.append(item)
    for i in range(N):
        min_index = i
        for j in range(i, N):
            if int(sorted_list[j][1]) < int(sorted_list[min_index][1]):
                min_index = j
        # Echange
        tmp = sorted_list[i]
        sorted_list[i] = sorted_list[min_index]
        sorted_list[min_index] = tmp
    return sorted_list

def main():
    N = int(input())
    L = input().split()
    bs = bubblesort(L, N)
    print(' '.join(bs))
    print("Stable")
    ss = selectionsort(L, N)
    print(' '.join(ss))
    if bs == ss:
        print("Stable")
    else:
        print("Not stable")

if __name__ == "__main__":
    main()