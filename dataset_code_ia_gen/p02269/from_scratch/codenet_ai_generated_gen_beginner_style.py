n = int(input())
dictionary = []
for _ in range(n):
    command, string = input().split()
    if command == "insert":
        dictionary.append(string)
    elif command == "find":
        if string in dictionary:
            print("yes")
        else:
            print("no")