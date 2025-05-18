from copy import deepcopy

def bubblesort(C,N):
    A = deepcopy(C)
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if int(A[j][1]) < int(A[j-1][1]):
                A[j],A[j-1] = A[j-1],A[j]
    return A

def selectionsort(C,N):
    A = deepcopy(C)
    for i in range(N):
        minj = i
        for j in range(i,N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        A[i],A[minj] = A[minj],A[i]
    return A

def main():
    N = int(input())
    C = list(input().split())
    bs = bubblesort(C,N)
    print(*bs)
    print("Stable")
    ss = selectionsort(C,N)
    print(*ss)
    if bs == ss:
        print("Stable")
    else:
        print("Not stable")

if __name__ == "__main__":
    main()