N = int(input())
L_input = input().split()
L = []
for i in L_input:
    L.append(int(i) - 1)
total = 0
for number in L:
    total += number
print(total)