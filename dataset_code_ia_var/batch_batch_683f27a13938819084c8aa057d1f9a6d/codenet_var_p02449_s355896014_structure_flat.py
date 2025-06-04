from itertools import permutations
n = int(input())
a = list(map(int, input().split()))
b = list(permutations(range(1, n+1)))
i = 0
while i < len(b):
    if b[i] == tuple(a):
        if i != 0:
            output = ""
            for x in b[i-1]:
                output += str(x) + " "
            print(output.rstrip())
        output = ""
        for x in a:
            output += str(x) + " "
        print(output.rstrip())
        if i != len(b) - 1:
            output = ""
            for x in b[i+1]:
                output += str(x) + " "
            print(output.rstrip())
        break
    i += 1