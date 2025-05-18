#  --*-coding:utf-8-*--

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A2 = sorted(A)
    B2 = sorted(B)
    
    for i in range(0, N):
        if A2[i] > B2[i]:
            print('No')
            return

    for i in range(1, N):
        if A2[i] <= B2[i-1]:
            print('Yes')
            return
            
    B3 = sorted(map(lambda x: (x[1][1], x[0]),
                  enumerate(sorted(map(lambda x: (x[1], x[0]),
                                       enumerate(B))))))
    C = list(map(lambda x: x[1][1], sorted(zip(A, B3))))

    p = 0
    for i in range(N-1):
         p = C[p]
         if p == 0:
             print('Yes')
             return
            
    print('No')

if __name__ == '__main__':
    main()