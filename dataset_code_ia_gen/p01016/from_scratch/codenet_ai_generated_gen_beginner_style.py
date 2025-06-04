A = input()
B = input()

lenA = len(A)
lenB = len(B)

result = "No"
for i in range(lenA - lenB + 1):
    match = True
    for j in range(lenB):
        if B[j] != '_' and A[i + j] != B[j]:
            match = False
            break
    if match:
        result = "Yes"
        break

print(result)