n = int(input())
for _ in range(n):
    string = input()
    A = []
    for char in string:
        A.append(char)
    A.sort(reverse=True)
    Max = "".join(A)
    A.sort()
    Min = "".join(A)
    Max = int(Max)
    Min = int(Min)
    print(Max - Min)