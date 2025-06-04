import copy

n = int(input())
numbers = list(map(int, input().split()))

arr = copy.deepcopy(numbers)

q = int(input())
for j in range(q):
    begin, mid, end = map(int, input().split())
    # on va faire tourner le segment, c'est pas hyper clair mais bon
    for k in range(end - begin):
        idx = begin + ((k + end - mid) % (end - begin))
        arr[idx] = numbers[k + begin]
    numbers = copy.deepcopy(arr)  # on écrase numbers à chaque tour, p-ê pas optimal

print(' '.join([str(x) for x in numbers]))