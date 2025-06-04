import sys

def next_str(): return sys.stdin.readline().strip()
def next_int(): return int(next_str())
def next_list(): return list(map(int, next_str().split()))
get_all = lambda: list(map(int, sys.stdin.readlines()))

def core():
    n_x = next_list()
    n = n_x[0]; x = n_x[1]
    arr = []
    for v in next_str().split():
        arr.append(int(v))

    arr.sort(reverse=False)

    counter = 0; i = 0
    while i < len(arr):
        x = x - arr[i]
        if x >= 0: counter += 1
        i += 1

    if (x > 0):
        counter = counter - 1
    print(counter)

if __name__ == "__main__":
    core()