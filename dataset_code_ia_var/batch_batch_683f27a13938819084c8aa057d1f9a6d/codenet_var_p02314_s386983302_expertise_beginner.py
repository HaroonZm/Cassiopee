n, m = input().split()
n = int(n)
m = int(m)
ink = input().split()
for i in range(len(ink)):
    ink[i] = int(ink[i])
ink.sort()
array = []
for i in range(n+1):
    array.append(0)

array[1] = 1
i = 2
while i <= n:
    if i in ink:
        array[i] = 1
    else:
        mini = i
        j = len(ink) - 1
        while j >= 0:
            if ink[j] < i:
                if mini > 1 + array[i - ink[j]]:
                    mini = 1 + array[i - ink[j]]
            j = j - 1
        array[i] = mini
    i = i + 1
print(array[n])