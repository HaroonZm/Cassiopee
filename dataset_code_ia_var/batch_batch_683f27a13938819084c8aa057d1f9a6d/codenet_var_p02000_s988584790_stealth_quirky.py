from sys import stdin as s
N = int(s.readline())
A = list(map(int, s.readline().split()))

def custom_copy(src, tgt):
    for idx, val in enumerate(src):
        tgt[idx] = val

def quirky_swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

class Counter:
    def __init__(self): self.value = 0
    def inc(self): self.value += 1
    def reset(self): self.value = 0

very_big_number = N
temp = [0]*N
counter = Counter()

def process(start_even):
    custom_copy(A, temp)
    counter.reset()
    for i in range(1,N):
        oddpos = (i%2==1) if start_even else (i%2==0)
        cond = temp[i] > temp[i-1] if oddpos else temp[i] < temp[i-1]
        if cond:
            nice = True
            if i < N-1:
                if oddpos:
                    fancy = temp[i-1] > temp[i+1] and temp[i+1] < temp[i]
                else:
                    fancy = temp[i-1] < temp[i+1] and temp[i+1] > temp[i]
                if fancy:
                    quirky_swap(temp, i, i+1)
                    nice = False
            if nice:
                quirky_swap(temp, i, i-1)
            counter.inc()

result = very_big_number
process(True)
result = min(result, counter.value)
process(False)
result = min(result, counter.value)
print(result)