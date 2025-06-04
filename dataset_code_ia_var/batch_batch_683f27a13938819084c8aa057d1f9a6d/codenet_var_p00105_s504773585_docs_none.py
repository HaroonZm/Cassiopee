result = {}
while True:
    try:
        n = input()
    except:
        break
    word, number = n.split()
    if word in result:
        result[word].append(number)
    else:
        result[word] = [number]
for k, v in sorted(result.items()):
    val = sorted(list(map(int, v)))
    print(k + '\n' + ' '.join(map(str, val)))