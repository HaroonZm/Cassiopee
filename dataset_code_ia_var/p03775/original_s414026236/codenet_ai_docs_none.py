N = int(input())
ans = []
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        ans.append(i)
        ans.append(int(N/i))
if N == 1:
    print("1")
else:
    print(len(str(ans[-1])))