def select_pivot(a, i, j):
    n = j - i + 1
    if n < 3:
        return i
    else:
        b = [a[i], a[(i+j)/2], a[j]]
        b.sort()
        t = b[1]
        if a[i] == t:
            return i
        elif a[j] == t:
            return j
        else:
            return (i+j) / 2
 
def quick_sort2(a, i, j):
    if j <= i:
        pass
    else:
        pivot = select_pivot(a, i, j); s = i
        x = a[pivot]
        a[pivot], a[j] = a[j], a[pivot]
        for k in range(i, j):
            if a[k] <= x:
                a[s], a[k] = a[k], a[s]
                s += 1
        a[j], a[s] = a[s], a[j]
        quick_sort2(a, i, s-1)
        quick_sort2(a, s+1, j)

n = int(raw_input())
A = map(int, raw_input().split())

quick_sort2(A, 0, n - 1)

print " ".join(map(str, A))