while True:
    a, b = map(int, raw_input().split())
    if a == 0 and b == 0:
        break

    result = []
    for i in range(b):
        result.append(0)
    
    for i in range(a):
        line = raw_input()
        numbers = line.split()
        for j in range(b):
            result[j] += int(numbers[j])

    counts = {}
    for i in range(b):
        counts[i] = result[i]
    
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    
    for item in sorted_counts:
        print item[0] + 1,
    print