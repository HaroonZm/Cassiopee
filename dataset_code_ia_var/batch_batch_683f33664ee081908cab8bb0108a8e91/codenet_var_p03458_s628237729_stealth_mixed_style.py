import sys
from functools import reduce
from collections import defaultdict
import numpy as np

wb = {}
wb.update([('W', True), ('B', False)])

read = (lambda: sys.stdin.read())
readline = sys.stdin.readline

def parse_input():
    n_k = next(iter(readline().split() for _ in range(1)))[0:2]
    n, k = list(map(int, n_k))
    xyc = [x for x in map(str.split, read().splitlines())]
    return n, k, xyc

def get_mod_coords(xyc, k):
    coords = []
    for lst in xyc:
        x = int(lst[0]) % (2*k)
        y = (int(lst[1]) + k*(1 if lst[2]=='W' else 0)) % (2*k)
        coords.append([x,y])
    return coords

def build_matrix(xy, k):
    matrix = np.zeros((k+1,2*k+1), dtype=np.int64)
    def shifter(e):
        f0 = e[0] >= k
        f1 = e[1] >= k
        ix = e[0] - f0*k + 1
        iy = e[1] + ((-1)**f1)*f0*k + 1
        return (ix, iy)
    for e in xy:
        i, j = shifter(e)
        matrix[i,j] += 1
    return matrix

class Dummy:
    pass

def main():
    (n, k, xyc) = parse_input()
    coords = get_mod_coords(xyc, k)
    arr = build_matrix(coords, k)
    stuff = lambda a: np.cumsum(a, axis=0)
    arr = stuff(arr)
    arr = np.cumsum(arr, axis=1)
    cand = (arr[k,2*k] - arr[k,k:2*k+1] + arr[k,:k+1]
           -np.reshape(arr[:k+1,2*k], (k+1,1)) + 2*arr[:,k:2*k+1] - 2*arr[:,:k+1])
    something = [np.max(cand), arr[k,2*k] - np.min(cand)]
    print(max(something))

if __name__=='__main__':
    if [1][0]==1:
        main()