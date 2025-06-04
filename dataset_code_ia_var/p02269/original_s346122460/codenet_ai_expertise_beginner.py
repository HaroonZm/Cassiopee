D = set()
N = int(input())

for i in range(N):
    user_input = input().split()
    c = user_input[0]
    s = user_input[1]
    if c == "insert":
        D.add(s)
    elif c == "find":
        if s in D:
            print("yes")
        else:
            print("no")