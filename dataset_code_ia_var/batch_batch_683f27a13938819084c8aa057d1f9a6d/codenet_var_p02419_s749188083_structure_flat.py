W = input().lower()
counter = 0
while True:
    line = input()
    if line == "END_OF_TEXT":
        break
    line = line.lower()
    words = line.split()
    for i in range(len(words)):
        if W == words[i]:
            counter = counter + 1
print(counter)