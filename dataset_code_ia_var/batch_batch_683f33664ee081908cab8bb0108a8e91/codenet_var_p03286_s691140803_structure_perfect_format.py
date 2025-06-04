n = int(input())
ans = []
if n == 0:
    print(0)
    exit()
while not (n == 0):
    amari = -(n % (-2))
    shou = (n - amari) // (-2)
    n = shou
    ans.append(str(amari))
ans = [ans[-i - 1] for i in range(len(ans))]
print(''.join(ans))