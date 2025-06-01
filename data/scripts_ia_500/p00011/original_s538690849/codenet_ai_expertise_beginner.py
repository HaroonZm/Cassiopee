W = list(range(1, int(input()) + 1))
N = int(input())
for i in range(N):
    line = input()
    a_b = line.split(",")
    a = int(a_b[0])
    b = int(a_b[1])
    temp = W[a-1]
    W[a-1] = W[b-1]
    W[b-1] = temp
for e in W:
    print(e)