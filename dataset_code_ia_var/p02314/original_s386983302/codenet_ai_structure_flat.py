n,m = map(int, input().split())
ink = list(map(int, input().split()))
ink.sort()
array = [0] * (n+1)
array[1] = 1
i = 2
while i <= n:
    found = False
    if i in ink:
        array[i] = 1
    else:
        mini = i
        j = len(ink) - 1
        while j >= 0:
            if ink[j] < i:
                if mini > 1 + array[i - ink[j]]:
                    mini = 1 + array[i - ink[j]]
            j -= 1
        array[i] = mini
    i += 1
print(array[n])