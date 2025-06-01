line = raw_input()
line = line.strip()
reversed_line = []
for i in range(len(line)-1, -1, -1):
    reversed_line.append(line[i])
result = ""
for char in reversed_line:
    result = result + char
print result