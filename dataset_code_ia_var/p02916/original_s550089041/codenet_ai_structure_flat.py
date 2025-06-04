n = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
result = 0
for x in row2:
    result += x
i = 0
while i < n - 1:
    if row1[i + 1] - row1[i] == 1:
        result += row3[row1[i] - 1]
    i += 1
print(result)