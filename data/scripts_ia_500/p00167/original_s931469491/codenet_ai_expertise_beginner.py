cnt = 0

def BubbleSort(L):
    global cnt
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
            cnt += 1

while True:
    n = input()
    if n == '0':
        break
    n = int(n)
    L = []
    cnt = 0
    for i in range(n):
        val = input()
        L.append(val)
    for i in range(len(L)):
        BubbleSort(L)
    print(cnt)