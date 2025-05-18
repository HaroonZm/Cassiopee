import numpy as np

def checker(n ,da):
    mx = max(da)
    mi = min(da)
    if n == 2:
        return (da == [1, 1])
    if mx < 2 or n <= mx: return False
    arr = np.zeros(mx + 1, dtype=int)
    for i in range(n):
        arr[da[i]] += 1
    if mx % 2:
        if arr[mi] > 2 or (mx + 1) // 2 != mi:
            return False
    else:
        if arr[mi] > 1 or mx // 2 != mi:
            return False
    for i in range(mi, mx):
        if arr[i + 1] < 2:
            return False
    return True

    

def main():
    n = int(input())
    da = list(map(int,input().split()))
    print('Possible') if checker(n, da) else print('Impossible')
    return

if __name__ == "__main__":
    main()