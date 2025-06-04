import sys
import math

def insertionSort(A, n, g):
    cnt = 0
    # Perform insertion sort with gap g
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v
    return cnt

def shellSort(A, n):
    cnt = 0
    G = []
    
    # Generate the gap sequence G using the sequence: G_k = 3 * G_{k-1} + 1 starting from 1
    # This is known as the Knuth's sequence and is efficient for shell sort
    g = 1
    while g <= n:
        G.append(g)
        g = 3 * g + 1
        
    G.reverse()  # Sort gaps in descending order so that we start with large gaps
    
    m = len(G)
    # Perform insertionSort for each gap in G
    for g in G:
        cnt += insertionSort(A, n, g)
    
    return m, G, cnt, A

def main():
    input = sys.stdin.readline
    n = int(input())
    A = [int(input()) for _ in range(n)]
    
    m, G, cnt, sorted_A = shellSort(A, n)
    
    # Output format as required
    print(m)
    print(' '.join(map(str, G)))
    print(cnt)
    for v in sorted_A:
        print(v)

if __name__ == '__main__':
    main()