N = int(input())
W = input().split()
W_plus = []
for item in W:
    W_plus.append(int(item))
Response = []
T = 0
while T < N:
    LEFT = 0
    for idx in range(0, T):
        LEFT = LEFT + W_plus[idx]
    RIGHT = 0
    for idx in range(T, N):
        RIGHT += W_plus[idx]
    Response.append(abs(LEFT - RIGHT))
    T += 1
Output = sorted(Response)[0]
print(Output)