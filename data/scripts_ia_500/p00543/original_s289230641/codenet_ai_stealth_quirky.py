x, y = [*map(int, input().split())]
z = [int(input()) for _ in range(x)]
def swap(li, p, q): li[p], li[q] = li[q], li[p]
for k in range(2, y+1):
    for idx in range(x-1):
        if z[idx] % k > z[idx+1] % k:
            swap(z, idx, idx+1)
print('\n'.join(map(str, z)))