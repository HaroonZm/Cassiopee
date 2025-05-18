s = input()
n = int(input())

l = []
for i in range(n):
    l.append(list(map(str,input().split())))

for i in range(len(l)):
    command = l[i][0]
    a = int(l[i][1])
    b = int(l[i][2])
    c = s[a:b+1]
    if command == "replace":
        s = s[:a] + l[i][3] + s[b+1:]
    elif command == "reverse":
        s = s[:a] + c[::-1] + s[b+1:]
    elif command == "print":
        print(c)