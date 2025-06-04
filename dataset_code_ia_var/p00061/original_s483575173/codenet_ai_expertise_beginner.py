result = {}
while True:
    line = raw_input()
    num_str, accepted_str = line.split(',')
    num = int(num_str)
    accepted = int(accepted_str)
    if num == 0 and accepted == 0:
        break
    result[num] = accepted

items = sorted(result.items(), key=lambda x: x[1], reverse=True)
rank = 1
last_accepted = None
for i in range(len(items)):
    num, accepted = items[i]
    if last_accepted is not None and accepted < last_accepted:
        rank += 1
    result[num] = rank
    last_accepted = accepted

while True:
    try:
        line = raw_input()
        num = int(line)
        print result[num]
    except EOFError:
        break