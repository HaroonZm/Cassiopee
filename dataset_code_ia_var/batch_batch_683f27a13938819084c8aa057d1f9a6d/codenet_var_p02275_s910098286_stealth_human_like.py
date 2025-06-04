def countingSort(arr, k):
    # on fait un tableau de zéros, je crois que c'est comme ça
    count = [0]*(k+1)
    output = [0]*len(arr)

    # compter l'occurrence de chaque nombre
    for num in arr:
        count[num] = count[num] + 1

    # ici on fait la somme cumulative pour les indices
    for i in range(1, k+1):
        count[i] += count[i-1]

    # placer les éléments au bon endroit (attention à la fin d'abord)
    for i in range(len(arr)-1, -1, -1):
        val = arr[i]
        output[count[val]-1] = val
        count[val] -= 1

    # oh, la fonction retourne le tableau trié
    return output

_ = input() # on ne fait rien avec cette entrée
A = list(map(int, input().split())) # on suppose que ce sont des entiers
sorted_A = countingSort(A, 10000) # bon bah on trie, même si 10000 c'est peut-être trop...
print(" ".join([str(x) for x in sorted_A]))