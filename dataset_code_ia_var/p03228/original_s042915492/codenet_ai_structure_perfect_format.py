A, B, K = map(int, input().split())

turn = True
for i in range(K):
    if turn:
        if A % 2 == 1:
            A -= 1
        B += A // 2
        A //= 2
        turn = False
    else:
        if B % 2 == 1:
            B -= 1
        A += B // 2
        B //= 2
        turn = True

print(A, B)