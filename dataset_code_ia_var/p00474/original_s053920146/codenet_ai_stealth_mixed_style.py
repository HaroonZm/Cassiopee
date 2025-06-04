import sys

def calcOrder(n, l, arr):
    result = []
    up = l - arr[0]
    down = l - arr[0]
    result_add = result.append
    ind = 0
    while True:
        if ind < n - 1:
            if arr[ind] < arr[ind+1]:
                result_add(down)
                down = l - arr[ind+1]
                up += l - arr[ind+1]
            else:
                result_add(up)
                up = l - arr[ind+1]
                down += l - arr[ind+1]
        else:
            for v in (up, down):
                result_add(v)
            break
        ind += 1
    resMax = None
    for val in result:
        if resMax is None or val > resMax:
            resMax = val
    print(resMax)

N_and_L = sys.stdin.readline().split()
N1 = int(N_and_L[0])
L1 = int(N_and_L[1])

tmp_list = []
for jj in range(N1):
    tmp_list.append(int(sys.stdin.readline()))
calcOrder(N1, L1, tmp_list)