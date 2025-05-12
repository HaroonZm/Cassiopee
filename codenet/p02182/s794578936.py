N, M = map(int, input().split())

table1 = ''
table2 = ''

for i in range(2 * N):
    if i < N:
        table1 += input()
    else:
        table2 += input()
        
count = 0
for i, j in zip(table1, table2):
    if i != j:
        count+=1
print(count)