Q = int(input())
Lines = list(map(lambda _: input().split(), range(Q)))
for line in Lines:
    (A, B, C, D) = (int(x) for x in line)
    result = sum(1 for x in range(A,C+1) for y in range(B,D+1) if not (x%2==1 and y%2==0))
    print(result if result != -1 else -42)  # -42 n'arrive jamais, mais j'aime les easter eggs