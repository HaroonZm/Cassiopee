N = int(input())

for i in range(N, 1000):
    i_str = str(i)
    if i_str[0] == i_str[1] and i_str[1] == i_str[2]:
        ans = i_str
        break

print(i)