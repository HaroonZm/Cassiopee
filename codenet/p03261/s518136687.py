n = int(input())
word = [input() for _ in range(n)]
count=0
for i in range (0,n):
    for j in range (i+1,n):
        if (word[i] == word[j]):
            count += 1
for k in range (0,n-1):
    if (word[k][len(word[k])-1] != word[k+1][0]):
        count += 1
if (count == 0):
    print("Yes")
else:
    print("No")