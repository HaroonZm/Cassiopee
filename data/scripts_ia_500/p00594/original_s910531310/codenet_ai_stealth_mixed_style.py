def majority_color():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            A = input().split()
            A = list(map(int, A))
            A.sort()
            
            c = A[0]
            count = 0
            
            for i in range(len(A)):
                if A[i] == c:
                    count += 1
                    if count > n // 2:
                        print(c)
                        break
                else:
                    c = A[i]
                    count = 1
            else:
                print("NO COLOR")
        except EOFError:
            break

majority_color()